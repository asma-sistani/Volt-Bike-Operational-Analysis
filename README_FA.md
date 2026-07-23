<div dir="rtl" align = "justify">

# 🚴 تحلیل عملیاتی VoltBike با پایتون <img src="Images/logo.png" alt="Logo" width="55" align="left"/>

---

![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0)

---

<div align = "center">

![Production Cost vs Customer Satisfaction](Visuals/cost_vs_satisfaction.png)
![Assembly Time vs Customer Satisfaction](Visuals/assembly_time_vs_satisfaction.png)

</div>

---

## معرفی پروژه
این پروژه یک تحلیل عملیاتی با پایتون است که بررسی می‌کند آیا بهینه‌سازی فرآیند تولید واقعاً به افزایش رضایت مشتری و ایجاد ارزش تجاری منجر می‌شود یا خیر. نتایج نشان می‌دهد تمرکز صرف بر کاهش زمان مونتاژ و افزایش هزینه تولید، اثر محدودی بر رضایت مشتری دارد. این تحلیل پیشنهاد می‌دهد که سرمایه‌گذاری در **نوآوری محصول** نسبت به بهینه‌سازی جزئی فرآیند، تصمیم منطقی‌تر و پربازده‌تری است.

**«به‌جای بهتر ساختن، متفاوت بسازید.»**
این پروژه با یک سؤال ساده شروع شد: اگر شرکت هزینه بیشتری صرف تولید کند و فرآیندها را بهبود ببخشد، آیا مشتریان واقعاً رضایت بیشتری خواهند داشت؟ نتایج نشان می‌دهد که نوآوری در محصول می‌تواند ارزش بلندمدت بیشتری نسبت به بهبودهای جزئی در فرآیندی که در حال حاضر هم عملکرد قابل‌قبولی دارد، ایجاد کند.

## سؤال بیزینسی

آیا VoltBike باید منابع بیشتری را صرف بهبود کارایی تولید کند، یا برای افزایش رضایت مشتری بر نوآوری محصول تمرکز نماید؟

---

## 🔎 انتظار اولیه در برابر واقعیت داده‌ها

**فرض اولیه:**
هزینه بیشتر در تولید و بهبود کارایی باید منجر به افزایش رضایت مشتری شود.

**آنچه داده‌ها نشان دادند:**
- زمان مونتاژ بین واحدها متغیر است، اما تأثیر قوی بر رضایت مشتری ندارد.
- هزینه تولید تنها رابطه متوسطی با رضایت دارد (R² ≈ 0.23).
- **فرصت بزرگ‌تر، نوآوری در محصول است، نه بهبودهای جزئی در فرآیند.**

---

## 🔍 یافته‌های کلیدی (نتیجه‌محور)

<div align = "center">

| یافته | مفهوم | تأثیر بر کسب‌وکار |
| ----- | ------ | ----------------- |
| میانگین زمان مونتاژ ≈ ۶۰ دقیقه، اما فقط ۱۶٪ در بازه ±۵٪ هستند | فرآیند کاملاً پایدار یا تکرارپذیر نیست | فضای بهبود وجود دارد، اما دستاوردها محدود است |
| R² = 0.23 (هزینه در مقابل رضایت) | هزینه تولید تنها ۲۳٪ تغییرات رضایت را توضیح می‌دهد | هزینه به‌تنهایی اهرم قوی برای افزایش رضایت نیست |
| همبستگی r ≈ 0.48 | هزینه و رضایت با هم حرکت می‌کنند، اما به‌طور متوسط | افزایش هزینه بازده نزولی دارد |
| رضایت مشتری ~۶.۵ برای همه مدل‌ها | مدل‌ها تفاوت معناداری در تجربه مشتری ندارند | تمرکز بر نوآوری و متمایزسازی باشد، نه اصلاحات کوچک |

</div>

---

## روش تحلیل

تحلیل در چهار مرحله انجام شد:
1. پاک‌سازی و اعتبارسنجی داده‌ها
2. تحلیل اکتشافی داده‌ها (EDA)
3. تحلیل نوسان و همبستگی
4. تفسیر تجاری نتایج آماری

---

## 🎯 پیام نهایی

**«به‌جای ساختن بهتر، متفاوت بسازید.»**
بودجه بهبود باید صرف **نوآوری** شود، نه بهینه‌سازی بی‌پایان فرآیندها.

---

## محدودیت‌ها

- مجموعه داده شبیه‌سازی‌شده است و نمایانگر داده‌های تجمیعی است.
- رضایت مشتری با یک شاخص عددی ساده اندازه‌گیری شده است.
- تحلیل تفکیکی بر اساس مدل دوچرخه می‌تواند نتایج دقیق‌تری ارائه دهد.

---

## 🚀 اقدامات راهبردی

<div dir="rtl" align = "center">
  <table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 12px; border: 1px solid #ddd; width: 46%; text-align: right;">اقدام</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 18%;">تأثیر</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 18%;">تلاش</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 18%;">اولویت</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">توسعه ویژگی‌های جدید محصول (به‌جای اصلاح مدل‌های فعلی)</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">⭐ زیاد</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">🔥 بالا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">جمع‌آوری بازخورد عمیق‌تر از مشتریان</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">حفظ استانداردهای فعلی تولید؛ فقط رفع مشکلات اساسی</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">کم</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">پرهیز از سرمایه‌گذاری سنگین در بهینه‌سازی بدون فایده</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">کم</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">کم</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">کم</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 📊 نکات برجسته تحلیلی

- پاک‌سازی دقیق مجموعه داده با حفظ الگوهای اصلی
- استفاده از IQR و بررسی‌های ثبات برای درک میزان نوسان نتایج
- مطالعه رابطه بین هزینه تولید، زمان مونتاژ و رضایت با استفاده از همبستگی و رگرسیون (R²)
- ایجاد نمودارهایی برای پشتیبانی از تصمیمات تجاری
- نگاه به نتایج از منظر عملیاتی، نه صرفاً آماری

---

## 🧮 نگاهی به عملکرد مونتاژ

- میانگین زمان مونتاژ ≈ ۶۰ دقیقه
- تنها ~۱۶٪ رکوردها در محدوده ±۵٪ میانگین
- تنها ~۳۲٪ رکوردها در محدوده ±۱۰٪ میانگین
- R² (زمان مونتاژ → رضایت) ≈ 0.018

📌 نوسان وجود دارد، **اما نگاه مشتری را به شکل معناداری تغییر نمی‌دهد.**
🔒 بنابراین **سرمایه‌گذاری سنگین برای بهینه‌سازی بیشتر زمان مونتاژ، از نظر اقتصادی توجیه‌پذیر نیست.**

---

## 🛠 ابزارها و مهارت‌های استفاده‌شده

<div align = "center">

| حوزه | ابزار / مهارت |
| ---- | -------------- |
| پایتون | pandas, numpy, matplotlib, seaborn |
| آمار | IQR، همبستگی، رگرسیون (R²) |
| کسب‌وکار | تبدیل تحلیل داده به تصمیمات عملی |
| بصری‌سازی | نمودارهای پراکندگی، جعبه‌ای و تحلیل واریانس |

</div>

---

## 📂 ساختار پروژه

<div dir="ltr">

```text
VoltBike_Analysis/
├─ Data/
│  └─ ebike_data.csv
├─ Images/
│  └─ logo.png
├─ Scripts/
│  ├─ cleaning.py
│  ├─ analysis.py
│  └─ visualization.py
├─ Results/
│  └─ final_data.csv
├─ Visuals/
│  ├─ avg_production_cost.png
│  ├─ avg_assembly_time.png
│  ├─ avg_customer_satisfaction.png
│  ├─ assembly_time_variability.png
│  ├─ customer_satisfaction_variability.png
│  ├─ cost_vs_satisfaction.png
│  ├─ assembly_time_vs_satisfaction.png
│  └─ Voltbike_Analysis_Animation.gif
├─ Executive_Summary/
│  ├─ VoltBike_Insight_Summary_FA.pdf
│  └─ VoltBike_Insight_Summary.pdf
├─ README.md
└─ README_FA.md
```

</div>

---

## داده‌ها

- **منبع:** داده‌های شبیه‌سازی‌شده تولید صنعتی
- **تعداد رکوردها:** ۲,۰۰۰
- **ستون‌ها:** `bike_type`, `production_cost`, `assembly_time`, `customer_score`

---

## ▶️ نحوه اجرای پروژه

<div dir="ltr">

```bash
python cleaning.py --input Data/ebike_data.csv --output Results/final_data.csv
python analysis.py --input Results/final_data.csv
python visualization.py
```

</div>

---

## 📁 خروجی‌های پروژه

👈 **خلاصه مدیریتی ([PDF – English](Executive_Summary/VoltBike_Operational_Analysis_Insight_Summary.pdf)):**
مروری ساختاریافته بر عملکرد عملیاتی، نوسان زمان مونتاژ، ارتباط هزینه تولید با رضایت مشتری، و اقدامات راهبردی پیشنهادی برای تمرکز بر نوآوری محصول.

👈 **خلاصه مدیریتی ([PDF – Persian](Executive_Summary/VoltBike_Operational_Analysis_Insight_Summary_FA.pdf)):**  
ترجمه فارسی خلاصه مدیریتی برای درک بهتر ذینفعان محلی.

👈 **نمایش پروژه ([Walkthrough – GIF](Visuals/Voltbike_Analysis_Animation.gif)):**
مروری مرحله‌به‌مرحله بر پوشه‌ها، کدهای اصلی و نمودارهای تحلیلی برای نمایش جریان کاری پروژه و نحوه استخراج بینش از داده‌ها.

---

## 👤 نویسنده

**اسما سیستانی — تحلیلگر داده**

💻 **GitHub:** [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/asma-sistani)

🔗 **LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asma-sistani)

🌐 **Portfolio:** [![Portfolio](https://img.shields.io/badge/Portfolio-2563EB?style=for-the-badge&logo=google-chrome&logoColor=white)](https://asmatheanalyst.github.io/portfolio.html)

---

**این پروژه نشان می‌دهد که «بهینه‌سازی بیشتر» همیشه بهترین مسیر نیست؛**
**گاهی نوآوری در محصول ارزش بسیار بیشتری خلق می‌کند.**

----

</div>