#!/usr/bin/env python3
"""
tiny_gnn.py — TANGO shrunk down to something you can read in one sitting.

tiny_surrogate.py used a single number to describe a structure. But a polymer
network's mechanics come from its *wiring* — what is bonded to what. You can't
squeeze a wiring diagram into one number, so we hand the model the whole graph
and let it learn. That is exactly what TANGO does, only TANGO's graphs are real
networks and its target is a full stress-strain curve.

Here:
   * each "material" is a small random network (nodes = molecules, edges = bonds),
   * each node's only feature is its degree (how many neighbors it has) — a purely
     topological quantity, just like TANGO's degree features,
   * the target is a made-up "stiffness" that depends on the topology,
   * a 2-layer graph convolutional network learns structure -> stiffness.

The lesson isn't this toy number; it's the *shape* of the pipeline:
graph in -> message passing -> pooling -> property out.

Install (once, ideally in a conda env — see modules/06_ai_for_materials.md):
    pip install torch torch_geometric matplotlib numpy
Run:
    python tiny_gnn.py
"""
import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv, global_mean_pool
try:                                             # PyG moved DataLoader over time
    from torch_geometric.loader import DataLoader
except ImportError:
    from torch_geometric.data import DataLoader

torch.manual_seed(0)
np.random.seed(0)


def make_network(n_nodes=12):
    """One random network + its (synthetic) stiffness that depends on topology."""
    p = np.random.uniform(0.15, 0.5)                  # connection probability
    A = (np.random.rand(n_nodes, n_nodes) < p).astype(int)
    A = np.triu(A, 1)
    A = A + A.T                                        # symmetric adjacency, no self-loops
    src, dst = np.nonzero(A)
    edge_index = torch.tensor(np.vstack([src, dst]), dtype=torch.long)

    deg = A.sum(axis=1)
    x = torch.tensor(deg, dtype=torch.float).view(-1, 1)     # node feature = degree

    density = A.sum() / (n_nodes * (n_nodes - 1))            # fraction of possible bonds
    stiffness = 1.5 * deg.mean() + 4.0 * density + np.random.normal(0, 0.1)
    y = torch.tensor([stiffness], dtype=torch.float)
    return Data(x=x, edge_index=edge_index, y=y)


# ---- build a dataset of many little networks --------------------------------
dataset = [make_network(np.random.randint(8, 16)) for _ in range(400)]
train, test = dataset[:320], dataset[320:]
train_loader = DataLoader(train, batch_size=32, shuffle=True)
test_loader = DataLoader(test, batch_size=64)


# ---- the model: graph in, one number out ------------------------------------
class TinyGNN(torch.nn.Module):
    def __init__(self, hidden=16):
        super().__init__()
        self.conv1 = GCNConv(1, hidden)      # mix each node with its neighbors
        self.conv2 = GCNConv(hidden, hidden) # mix again -> reaches 2-hop neighborhoods
        self.head = torch.nn.Linear(hidden, 1)

    def forward(self, data):
        x = F.relu(self.conv1(data.x, data.edge_index))
        x = F.relu(self.conv2(x, data.edge_index))
        x = global_mean_pool(x, data.batch)  # squash all nodes -> one vector per graph
        return self.head(x).view(-1)


model = TinyGNN()
opt = torch.optim.Adam(model.parameters(), lr=0.01)

# ---- train ------------------------------------------------------------------
for epoch in range(1, 61):
    model.train()
    total = 0.0
    for batch in train_loader:
        opt.zero_grad()
        pred = model(batch)
        loss = F.mse_loss(pred, batch.y)
        loss.backward()
        opt.step()
        total += loss.item() * batch.num_graphs
    if epoch % 10 == 0:
        print(f"  epoch {epoch:3d}   train MSE {total/len(train):.4f}")

# ---- test -------------------------------------------------------------------
model.eval()
preds, trues = [], []
with torch.no_grad():
    for batch in test_loader:
        preds.append(model(batch))
        trues.append(batch.y)
preds = torch.cat(preds).numpy()
trues = torch.cat(trues).numpy()
mae = np.mean(np.abs(preds - trues))
print(f"\n  held-out mean absolute error: {mae:.4f}")
print("  the GNN learned to read stiffness off the wiring diagram alone.\n")

# ---- parity plot ------------------------------------------------------------
try:
    import matplotlib.pyplot as plt
    lo, hi = trues.min(), trues.max()
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    ax.plot([lo, hi], [lo, hi], "k--", lw=1)
    ax.scatter(trues, preds, s=18, color="#4E2A84", alpha=0.6)
    ax.set_xlabel("true stiffness")
    ax.set_ylabel("GNN prediction")
    ax.set_title("tiny GNN: topology -> property")
    fig.tight_layout()
    fig.savefig("tiny_gnn.png", dpi=150)
    print("  saved figure -> tiny_gnn.png\n")
except ImportError:
    pass
