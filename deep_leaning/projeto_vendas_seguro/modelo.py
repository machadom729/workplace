import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


# carregando os dados de treino e teste
dados_train = pd.read_csv('datasets/vendas_data_training.csv', dtype=float)
x_train = dados_train.drop('total_vendas', axis=1).values
y_train = dados_train[['total_vendas']].values

dados_test = pd.read_csv('datasets/vendas_data_test.csv', dtype=float)
x_test = dados_test.drop('total_vendas', axis=1).values
y_test = dados_test[['total_vendas']].values

# escalando os dados
x_scaler = MinMaxScaler(feature_range=(0, 1))
y_scaler = MinMaxScaler(feature_range=(0, 1))

x_scaled_treino = x_scaler.fit_transform(x_train)
y_scaled_treino = y_scaler.fit_transform(y_train)

x_scaled_test = x_scaler.transform(x_test)
y_scaled_test = y_scaler.transform(y_test)

# estruturando o model0

# definindo hiperparametros
learning_rate = 0.001
num_epochs = 100
display_step = 5

# definindo inputs e outputs
num_inputs = 9
num_outputs = 1

# camadas
layer_1_nodes = 50
layer_2_nodes = 100
layer_3_nodes = 50

# construindo as camadas da rede
model = Sequential()
model.add(Input(shape=(None, num_inputs)))
model.add(Dense(layer_1_nodes, activation='relu'))
model.add(Dense(layer_2_nodes, activation='relu'))
model.add(Dense(layer_3_nodes, activation='relu'))
model.add(Dense(num_outputs, activation=None))

# compilando o model
adam = Adam(learning_rate=learning_rate)

model.compile(optimizer=adam, loss='mse', metrics=['mse'])
model.summary()

# treinando o modelo
callback1 = EarlyStopping(monitor='val_loss', patience=10)
callback2 = ModelCheckpoint(filepath='save', monitor='val_loss',
                            save_best_only=True)

model.fit(x=x_scaled_treino, y=y_scaled_treino, epochs=num_epochs,
          callbacks=[callback1, callback2],
          validation_data=(x_scaled_test, y_scaled_test))