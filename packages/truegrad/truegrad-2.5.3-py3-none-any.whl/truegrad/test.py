import torch
import optim
import time
from lion_pytorch import Lion

a = torch.nn.Sequential(torch.nn.Linear(10, 128), torch.nn.ReLU(), torch.nn.LayerNorm(128), torch.nn.Linear(128, 10))
# o = torch.optim.Adam(a.parameters(), lr=0.1)
o = optim.Graft(a.parameters(), torch.optim.Adam(a.parameters(), lr=0.1), Lion(a.parameters(), lr=1))

for i in range(10000):
    inp = torch.randn((1024, 10))
    out = (a(inp) - inp.square()).abs().mean()
    out.backward()
    o.step()
    o.zero_grad()
    print(f'{i:05d} - {out.item():8.6f}')
