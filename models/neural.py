import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import trange


class MultiOutputNeuralNetwork(nn.Module):
  def __init__(self,input_dim=943,output_dim=4760):
    super().__init__()
    self.hidden1 = nn.Linear(input_dim,int(input_dim/2))
    self.activation1 = nn.Sigmoid()
    self.hidden2 = nn.Linear(int(input_dim/2),int(input_dim/4))
    self.activation2 = nn.Sigmoid()
    self.output = nn.Linear(int(input_dim/4),output_dim)
  
  def forward(self,x):
    x = self.hidden1(x)
    x = self.activation1(x)
    x = self.hidden2(x)
    x = self.activation2(x)
    x = self.output(x)
    return x
   
   
def train_nn(params= {},data={}):
    epochs = params["epoch"]
    lr = params["lr"]
    batch_size = params["batch_size"]
    X,y = data['X'],data['y']
    dataset_size = len(data['y'])
    model =  MultiOutputNeuralNetwork(input_dim=params["input_dim"],output_dim=params["output_dim"])
    loss_fn = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(),lr=lr)
    losses = []
    for epoch in trange(epochs):
        batch_loss = []
        for batch_number in (0,dataset_size,batch_size):
            start_index = batch_number
            end_index = start_index + batch_size
            if end_index > dataset_size:
                end_index = dataset_size
            X_batch = torch.tensor(X[start_index:end_index],dtype=torch.float32)
            y_batch = torch.tensor(y[start_index:end_index],dtype=torch.float32)
            y_pred = model(X_batch)
            loss = loss_fn(y_pred, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            batch_loss.append(loss.item())
        epoch_loss = torch.mean(batch_loss)
        losses.append(epoch_loss)
        print(f'epoch={epoch} epoch_loss={epoch_loss}')
    plot_and_save(x=range(losses),y = losses,filename="nn_loss.png") 
    return model,losses


