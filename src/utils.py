import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils import shuffle

def plot_cat_target(df, colname, target= 'G3', figsize = (8,5)):
    """_
    Vẽ boxplot so sánh các biến catgorical với biến target G3
    """
    plt.figure(figsize=figsize)
    sns.boxplot(x = colname, y = target, data=df, palette="Set2", hue = colname, legend=False)
    plt.title(f"Ảnh hưởng của {colname} đến với {target}")
    plt.show()
    
def plot_correlation_heatmap(df, num_cols):
    """
    Vẽ heatmap các biến Numerical (Ordinal) 
    """
    
    corr_matrix = df[num_cols].corr(method='spearman')
    
    plt.figure(figsize=(12,10))
    
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    sns.heatmap(corr_matrix,
                mask= mask,
                annot = True,
                fmt = ".2f",
                cmap = "coolwarm",
                vmin=-1, vmax=1,
                center=0,
                linewidths=0.5,
                cbar_kws={"shrink" : .8})
    
    plt.title(f"Biểu đồ tương quan của các biến cột Numerical (Ordinal)")
    plt.show()
    
    
def plot_line_grid(df, ordinal_cols, target = 'G3', n_cols = 3):
    
        
    n_vars = len(ordinal_cols)
    n_rows = math.ceil(n_vars / n_cols)
    
    fig, axes  = plt.subplots(n_rows, n_cols, figsize= (n_cols*5, n_rows*5))
    
    axes = axes.flatten()
    
    for i, col in enumerate(ordinal_cols):
        sns.lineplot(x=col, y=target, data=df, ax=axes[i], 
                     marker='o', color='red', linewidth=2.5)
        
        axes[i].set_title(f"Tác động của {col}", fontsize=12)
        axes[i].set_xlabel(col, fontsize=10)
        axes[i].set_ylabel("G3")
        
        axes[i].grid(True, linestyle='--', alpha=0.7)
        
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()
        
    
def plot_cat_grid(df, cat_cols, target = 'G3', n_cols = 3):
    """
    Vẽ grid các boxplot cho các biến categorical
    """
    
    n_vars = len(cat_cols)
    n_rows = math.ceil(n_vars / n_cols)
    
    fig, axes  = plt.subplots(n_rows, n_cols, figsize= (n_cols*5, n_rows*5))
    
    axes = axes.flatten()
    
    for i, col in enumerate(cat_cols):
        
        sns.boxplot(x = col, y = target, data= df, palette="Set2", hue=col, legend=False, ax = axes[i])
        
        axes[i].set_title(f"Tác động của {col} đến biến {target}")
        axes[i].set_xlabel('')
        axes[i].set_ylabel(target)
        
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
            
    plt.tight_layout()
    plt.show()
    
def plot_ordinal_grid(df, or_cols, target = 'G3', n_cols = 3):
    """
    Vẽ grid boxplot của các biến Ordinal
    """
    n_vars = len(or_cols)
    n_rows = math.ceil(n_vars / n_cols)
    
    fig, axes  = plt.subplots(n_rows, n_cols, figsize= (n_cols*5, n_rows*5))
    
    axes = axes.flatten()
    
    for i, col in enumerate(or_cols):
        
        sns.boxplot(x = col, y = target, data= df, palette="Set2", hue=col, legend=False, ax = axes[i])
        sns.pointplot(x = col, y= target, data = df, ax=axes[i], color='red', markers='o', errorbar=None)
        
        axes[i].set_title(f"Tác động của {col} đến biến {target}")
        axes[i].set_xlabel('')
        axes[i].set_ylabel(target)
        
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
            
    plt.tight_layout()
    plt.show()
    
def statistical_testing(df, cat_col, target = 'G3'):
    """
    Hàm kiểm tra dùng T-test hoặc ANOVA dự trên số nhóm
    """
    print("-" * 20)
    groups = df.groupby(cat_col)[target].apply(list)
    
    if len(groups) == 2:
        stat, p_value = stats.ttest_ind(groups.iloc[0], groups.iloc[1])
        test_type = "T-test"
        
    else:
        stat, p_value = stats.f_oneway(*groups)
        test_type = "ANOVA"
        
    print(f"\nKiểm định cột {cat_col}")
    print(f"Loại test: {test_type}")
    print(f"P-value: {p_value:3f}")
        
    if p_value < 0.05:
        print(f"Có sự ảnh hưởng (Sự khác biệt có ý nghĩa thống kê)\n")
        return 1
    else:
        print(f"Không ảnh hưởng (Sự khác biệt chỉ là ngẫu nhiên)\n")
        return 0
        
def evalutate_model(model_name, y_true, y_pred):
    print(f"Model: {model_name}")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")
    print(f"Classification report: \n{classification_report(y_true, y_pred)}")


def oversampling_train_data(X_train, y_train):
    train_data = pd.concat([X_train, y_train], axis=1).reset_index(drop=True)
    
    target_col = 'is_high_risk'
    
    majority_class = train_data[train_data[target_col] == 0]
    minority_class = train_data[train_data[target_col] == 1]
    
    # Oversampling
    minority_upsampled = minority_class.sample(n=len(majority_class), replace=True, random_state=33)
    
    # Gộp vào data mới
    train_data_new = pd.concat([majority_class, minority_upsampled])
    train_data_new = shuffle(train_data_new, random_state=33)  
    
    y_train_resampled = train_data_new[target_col]
    X_train_resampled = train_data_new.drop(target_col, axis=1)  
    
    return X_train_resampled, y_train_resampled
    
def confusion_matrix_plot(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)

    # Vẽ Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, 
                xticklabels=['Low Risk (0)', 'High Risk (1)'],
                yticklabels=['Low Risk (0)', 'High Risk (1)'])

    plt.xlabel('Predicted Label')
    plt.ylabel('Actual Label')
    plt.title('Confusion Matrix - Logistic Regression')
    plt.show()
    
    
    