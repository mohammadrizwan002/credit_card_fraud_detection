💳 Credit Card Fraud Detection using Machine Learning(This is the project for AI&ML Internship)

🔍 Objective
Build a machine learning model to detect fraudulent credit card transactions using both supervised and unsupervised algorithms, and provide a user-friendly interface through a web app.

---

📊 Dataset
- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Total transactions: 284,807
- Fraudulent cases: 492
- Features: 30 numerical features (`V1` to `V28`, `Amount`, `Time`)
- Target column: `Class` (0 = Normal, 1 = Fraud)

---

🧠 Algorithms Used
- Isolation Forest (Unsupervised)
- Local Outlier Factor (Unsupervised)
- XGBoost Classifier (Supervised)

---

🧰 Tools & Libraries
- Python
- Pandas, NumPy
- scikit-learn, XGBoost
- Matplotlib, Seaborn
- Google Colab
- Streamlit (for web app)

---

⚙️ How to Run the Project

🔬 Model Training
1. Download `creditcard.csv` from Kaggle.
2. Place it inside the `data/` folder (locally only).
3. Open `fraud_detection.ipynb` using Google Colab.
4. Run all cells to:
   - Preprocess the data
   - Train using Isolation Forest, LOF, and XGBoost
   - Evaluate models
   - Save trained model as `xgboost_model.pkl` inside the `model/` folder

🌐 Web App (Streamlit)
1. Open terminal or command prompt.
2. Navigate to the `streamlit_app` directory
3.Run the Streamlit app: streamlit run app.py,
4.The app will open in your browser (usually at http://localhost:8501).

5.Enter 30 feature values to check if the transaction is fraudulent
   cd streamlit_app.

🧑‍💻 Author
V Mohammad Rizwan 
AIML Internship Project – June 2025 ✅
