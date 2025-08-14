# 🏠 Real Estate Price Prediction

This project implements a machine learning solution to predict real estate prices using a real-world housing dataset. The project includes data preprocessing, model training with Linear Regression, and deployment through a modern web application using Streamlit.

## 🚀 Live Demo

**Web Application:** [https://houses-price-prediction.streamlit.app/](https://houses-price-prediction.streamlit.app/)

## Project Structure

```
Real Estate Price Prediction/
│
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── requirements.txt            # Python dependencies
├── Dataset/
│   └── estate-data.csv         # Real estate dataset
├── Notebook/
│   └── analysis.ipynb          # Jupyter notebook with complete analysis
├── Application/
│   ├── app.py                  # Streamlit web application
│   ├── scaler.pkl              # Saved StandardScaler for data preprocessing
│   └── model.pkl               # Saved trained Linear Regression model
├── Saved Models/
│   ├── scaler.pkl              # (optional) Saved StandardScaler
│   └── model.pkl               # (optional) Saved trained model
```

## Dataset

The project uses a real estate dataset containing features such as:
- **bed**: Number of bedrooms
- **bath**: Number of bathrooms
- **house_size**: House size in square feet
- **city**: City name
- **state**: State name
- **price**: Target variable (house price)
- ...and more

## Workflow

1. **Data Collection and Analysis**
   - Load and explore the real estate dataset
   - Analyze data distribution and statistics
   - Check for missing values and data quality

2. **Data Preprocessing**
   - Drop irrelevant columns and handle missing values
   - Feature standardization using StandardScaler
   - Separate features (X) and target (y)

3. **Train-Test Split**
   - Split data into training and testing sets (80/20 split)
   - Random state for reproducibility

4. **Model Training**
   - Linear Regression model
   - Train the model on standardized training data

5. **Model Evaluation**
   - Metrics: Mean Squared Error, R² Score
   - Assess model performance on test data

6. **Model Deployment**
   - Save trained model and scaler using joblib
   - Deploy interactive web application using Streamlit

## Key Features

### 🤖 Machine Learning Pipeline
- **Data Standardization**: Uses StandardScaler to normalize features
- **Linear Regression**: Predicts house prices based on input features
- **Model Persistence**: Joblib serialization for model and scaler saving/loading

### 💻 Prediction System

- **Streamlit Web Application** (`Application/app.py`):
  - Modern UI for user-friendly predictions
  - Number inputs for bedrooms, bathrooms, and house size
  - Instant price prediction results

## Installation & Usage

### Prerequisites
```bash
pip install pandas numpy scikit-learn streamlit matplotlib joblib
```

### 💻 Run Locally

#### Running the Jupyter Notebook
```bash
jupyter notebook Notebook/analysis.ipynb
```

#### Launching Web Application Locally
```bash
cd Application
streamlit run app.py
```

## 🎯 Model Performance

- **Algorithm**: Linear Regression
- **Features Used**: `bed`, `bath`, `house_size`
- **Evaluation**: Mean Squared Error, R² Score

## 📝 Input Format

For making predictions in the web app, provide:
- Number of bedrooms
- Number of bathrooms
- House size (sq ft)

## ✨ Web Application Features

- **Modern Design**: Clean and intuitive interface
- **Instant Results**: Real-time price prediction
- **Reusable Models**: Easily update with new data

## 🛠 Technologies Used

- **Python 3.x**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib**
- **Jupyter Notebook**
- **Matplotlib**

## 🌐 Deployment

The application is deployed on **Streamlit Community Cloud**:  
[House Price Predictor](https://houses-price-prediction.streamlit.app/)

## 🔮 Future Enhancements

- [ ] Add more advanced regression models (e.g., XGBoost, LightGBM)
- [ ] Implement feature selection and engineering
- [ ] Add interactive data visualization in the web app
- [ ] Enable batch predictions and CSV uploads
- [ ] Deploy to additional cloud platforms

## 👨‍💻 Developer

**Daivagna Parmar**  
- 📧 **Email** : [devparmar1895@gmail.com](mailto:devparmar1895@gmail.com)
- 🔗 **GitHub** : [@daivagnaa](https://github.com/daivagnaa)
- 💼 **LinkedIn** : [Daivagna Parmar](https://in.linkedin.com/in/daivagna-parmar-949315316)

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for suggestions and improvements.

---

*This project demonstrates a complete machine learning pipeline from data preprocessing to model deployment, showcasing practical implementation of real estate price prediction with a user-friendly web interface.*

**⭐ Star this repository if you found it helpful!**