from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':

    dataframes = extract_from_excel('data/input')
    print(type(dataframes))
    dataframes_ct = concat_data_frames(dataframes)
    print(type(dataframes_ct))
    load_excel(dataframes_ct, 'data/output', 'output')
    print("Done!")
