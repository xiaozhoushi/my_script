import pandas as pd

def main():
    csv_path = '~/Documents/data/GIANA_challenge/class/m_train/train.csv'
    txt_path = './train.txt'
    df = pd.read_csv(csv_path, skiprows = 0, usecols=['image_id','Histologia'])
    num = df.shape[0]
    for i in range(50):
        print('id', df.iat[i, 0],'lb', df.iat[i, 1])

if __name__ == '__main__':
    main()
