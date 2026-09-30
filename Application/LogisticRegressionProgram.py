
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class LRClass():

    def predect_result(input_feature,target_feature,test_size_param=0.2,radom_state_param=30):
        X = input_feature
        y = target_feature

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(X)

        X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=test_size_param,
        random_state=radom_state_param,
        stratify=y
        )

        model = LogisticRegression()
        model.fit(X_train,y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test,y_pred)

        print("accuracy:",accuracy)

        return [model,vectorizer]