from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess(data):
    le = LabelEncoder()
    data['Geography'] = le.fit_transform(data['Geography'])
    data['Gender'] = le.fit_transform(data['Gender'])

    X = data.drop(['RowNumber','CustomerId','Surname','Exited'], axis=1)
    y = data['Exited']

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y
