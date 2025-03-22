from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

def select_best_features(data = None,params = {}):
    if params["method"] == "PCA":
        # Step 1: Apply PCA
        pca = PCA(n_components=params["num_comp"])  # Select top n principal components
        pca.fit(data)

        # Step 2: Get PCA loadings (importance of each feature in principal components)
        pca_df = pd.DataFrame(pca.components_, columns=data.columns)

        # Step 3: Select the top contributing original features
        top_features = pca_df.abs().sum().nlargest(params["num_features"]).index  # Select top 2 features
        print("Top contributing features:", top_features)
        
        return top_features

        
    elif params["method"] == "kbest":
        selector = SelectKBest(score_func=f_regression, k=2)
        X_new = selector.fit_transform(data['X'], data['y'])
    elif params['method'] == 'rfe':
        # Step 1: Choose a regression model
        model = LinearRegression()

        # Step 2: Apply Recursive Feature Elimination (RFE)
        rfe = RFE(model, n_features_to_select=2)  # Select top 2 features
        rfe.fit(X, y)

        # Step 3: Get selected feature names
        selected_features = X.columns[rfe.support_]
        print("Selected Features:", selected_features)

        return selected_features
                
