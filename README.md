# Project Student Alcohol Consumption Analysis
## **Project overview**
Dự án tập trung phân tích các tác động như việc tiêu thụ rượu bia, nền tảng gia đình và các yếu tố xã hội đến với kết quả học tập của học sinh trung học. Sử dụng bộ dữ liệu *Sudent Alcohol Consumption*, nhóm thực hiện Phân tích dữ liệu và xây dựng mô hình học máy cho các câu hỏi chi tiết.

## **Team info**
| MSSV | Họ và tên |
| --------- | --------- |
| 22120117 | Trần Mạnh Hùng |
| 23120025 | Phan Thị Phương Chi |
| 23120060 | Trần Kim Ngân |

## **Data source and description**
- Nguồn dữ liệu: [Student Alcohol Consumption](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption)
- Bối cảnh: Dữ liệu được thu nhập qua khảo sát học sinh tham gia các khoá học Toán và tiếng Bồ Đào Nha tại 2 trường trung học.

## **Research questions list**
- Extra support có giúp học sinh tăng điểm (G3) hay không, tăng bao nhiêu?

- Dự đoán học sinh có nguy cơ rớt môn dựa trên các yếu tố hành vi  (romantic, goout, Dalc, Walc, health, freetime) và G1,G2

- Mối liên hệ giữa các yếu tố nhân khẩu học (như Giới tính, Tuổi tác) và thói quen học tập (Studytime) ảnh hưởng như thế nào đến Hiệu suất Học tập (Learning Efficiency) trong các môn học?

- Phân tích tác động hai mặt của Internet đối với kết quả học tập (G3) khi xét ảnh hưởng của thời gian rảnh (freetime) và thói quen đi chơi (goout).

- Các yếu tố về gia đình (như famsize, Medu, Fedu,...) có ảnh hưởng đến kết quả học tập (G3) của một học sinh hay không?

- Dựa vào thói quen của học sinh có thể dự đoán họ có trở nên uống rượu nhiều hơn hay không?

## **Key findings summary**

- **Hành vi tiêu thụ cồn:** Có mối tương quan dương mạnh giữa uống rượu ngày thường và cuối tuần. Những học sinh có chỉ số `total_alc` cao thường có xu hướng nghỉ học nhiều hơn (absences cao) và điểm số thấp hơn nhẹ.

- **Ảnh hưởng của phụ huynh:** nền tảng gia đình (`Fedu`, `Medu`, `Fjob`, `Mjob`) có ảnh hưởng nhiều đến điểm số của học sinh

## **File structure explaination**

```
student_alcohol_consumption_DS/
├── data/                               # Chứa dữ liệu gốc và dữ liệu đã được xử lý
├── notebooks/
│   ├── 01_data_collection.ipynb        # Mô tả, thu nhập dữ liệu
│   ├── 02_data_exploration.ipynb       # Phân tích dữ liệu
│   ├── 03_data_preprocessing.ipynb     # Tiền xử lý chung bộ dữ liệu (giải quyết missing value, outliers...)
│   └── 04_questioning.ipynb            # Đặt các câu hỏi, phân tích và trả lời
├── .gitignore
└── README.md
```

## **How to run instructions**
**Tạo môi trường ảo**
```bash
# Trên Windows
python -m venv venv
venv\Scripts\activate
```

**Tải thư viện và khởi động**
```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Khởi động Jupyter Notebook
jupyter notebook
```

1. Mô tả, thu nhập dữ liệu
- File: `notebooks/01_data_collection.ipynb` 
- Cách chạy: Mở file chọn `Kernel` $\rightarrow$ `Restart & Run All`
2. Phân tích dữ liệu
- File: `notebooks/02_data_exploration.ipynb`
- Cách chạy: Mở file chọn `Kernel` $\rightarrow$ `Restart & Run All`
3. Tiền xử lý chung bộ dữ liệu
- File `notebooks/03_data_preprocessing.ipynb`
- Cách chạy: Mở file chọn `Kernel` $\rightarrow$ `Restart & Run All`
4. Phân tích và trả lời câu hỏi
- File `notebooks/04_questioning.ipynb`
- Cách chạy: Mở file chọn `Kernel` $\rightarrow$ `Restart & Run All`

## **Dependencies list**
Các thư viện sử dụng: `scipy`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `statsmodels`
