import pandas as pd
from app.pipeline.transform import concat_data_frames

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def testar_a_concatenação_de_lista_df():
    #Use o arrange, act e o assert para realizar os testes da função concat_data_frames
    lista_df = [df_1, df_2]

    #arrange
    arrange = pd.concat(lista_df, ignore_index=True)

    #act
    act = concat_data_frames(lista_df)
    
    #assert
    assert act.shape == (4,2)
    assert arrange.equals(act)
    assert act.shape != (5,2)
