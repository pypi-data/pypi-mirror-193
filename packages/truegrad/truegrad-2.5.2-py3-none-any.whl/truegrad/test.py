import torch
import optim
import time

a = torch.nn.Linear(10, 2)
o = optim.Graft(a.parameters(), torch.optim.Adam(a.parameters(), lr=0.01), torch.optim.SGD(a.parameters(), lr=1))

for i in range(1000):
    a(torch.randn((16, 10))).mean().backward()
    o.step()
    o.zero_grad()
    print(i, a.weight.norm().item())
    time.sleep(0.1)
