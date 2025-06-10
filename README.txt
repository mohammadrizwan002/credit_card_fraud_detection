Credit Card Fraud Detection using Machine Learning

🔍 Objective
Build a machine learning model to detect fraudulent credit card transactions using supervised and unsupervised algorithms.

🧠 Algorithms Used
- Isolation Forest
- Local Outlier Factor
- XGBoost Classifier

📊 Dataset
- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Features are PCA-transformed, with "Class" as the target (1 = Fraud, 0 = Normal)

🧰 Tools & Libraries
- Python, Pandas, NumPy
- scikit-learn, XGBoost
- Matplotlib, Seaborn
- Google Colab

⚙️ How to Run
1. Upload the `creditcard.csv` file into the `data/` folder.
2. Open `fraud_detection.ipynb` in Google Colab.
3. Run all cells to execute preprocessing, training, evaluation, and model saving.

🧪 Output
- High precision & recall on fraud detection
- Visual confusion matrix
- Trained model saved as `xgboost_model.pkl`


