# Feature Engineering

## 1. What Is Feature Engineering?

**Feature engineering** is the process of using domain knowledge to create, transform, or select features from raw data to improve the performance of Machine Learning models.

**Example:** From a `date_of_birth` column, we can extract a new feature called `age`.

Raw Data → Feature Engineering → Useful Features → ML Model

---

## 2. Types of Feature Engineering

Feature engineering can be divided into four major categories:

```text
                 FEATURE ENGINEERING
                         |
          +--------------+--------------+
          |              |              |
    Transformation   Construction   Selection
          |              |              |
      Modify existing  Create new     Choose the
        features       features      most useful ones
                         |
                    Extraction
                         |
                 Extract information
                 or representations
```

### 1. Feature Transformation

**Definition:** Changing the format, scale, or distribution of existing features without fundamentally changing the information they represent.

**Common techniques:**

| Technique | Purpose | Example |
|---|---|---|
| Missing Value Imputation | Fill missing values | Replace missing age with the median |
| Categorical Encoding | Convert categories into numbers | `Red, Blue` → numerical representations |
| Outlier Handling | Identify and handle extreme values | Cap unusually high salaries |
| Feature Scaling | Bring features to comparable scales | StandardScaler, MinMaxScaler |
| Log Transformation | Reduce right skewness | `income` → `log(income)` |

**Example:**

```python
# Before transformation
age = [20, 25, None, 30]

# After median imputation
age = [20, 25, 25, 30]
```

**Goal:** Make existing features more suitable for ML algorithms.

---

### 2. Feature Construction

**Definition:** Creating new features from existing features using domain knowledge or mathematical operations.

**Examples:**

| Existing Features | New Feature |
|---|---|
| Date of birth | Age |
| Height, Weight | BMI |
| Price, Quantity | Total Amount |
| Last purchase date | Days Since Last Purchase |
| Length, Width | Area |

**Example:**

```python
df["total_amount"] = df["price"] * df["quantity"]
```

**Goal:** Provide the model with useful information that may not be directly available in the original dataset.

---

### 3. Feature Selection

**Definition:** Selecting the most relevant features and removing irrelevant, redundant, or unhelpful features.

**Common techniques:**

- **Filter Methods:** Correlation, statistical tests, variance threshold.
- **Wrapper Methods:** Forward selection, backward elimination, Recursive Feature Elimination (RFE).
- **Embedded Methods:** Lasso regression, tree-based feature importance.

**Example:**

Suppose we want to predict house prices.

```text
Useful features:
✓ Area
✓ Number of bedrooms
✓ Location

Potentially unhelpful feature:
✗ Unique row identifier
```

**Goal:** Reduce unnecessary complexity, improve efficiency, and potentially improve generalization.

*Note: A feature should not be removed simply because it has a low correlation with the target. Its usefulness depends on the model and the relationships in the data.*

---

### 4. Feature Extraction

**Definition:** Transforming existing data into a new set of features that captures useful information.

Feature extraction is especially useful when working with high-dimensional or unstructured data, such as images and text.

**Examples:**

| Data | Feature Extraction Technique |
|---|---|
| Images | CNNs extract visual patterns |
| Text | TF-IDF, word embeddings |
| High-dimensional numerical data | PCA |
| Audio | MFCCs, spectrogram-based representations |

**Example:**

A raw image contains thousands of pixel values. A Convolutional Neural Network (CNN) can learn useful representations such as edges, textures, and shapes.

```text
Raw Image → CNN → Extracted Features → Classifier → Prediction
```

**Goal:** Represent complex data in a form that helps an ML model learn useful patterns.

---

## 3. Feature Construction vs Feature Extraction

These concepts sound similar, but they are different.

| Feature Construction | Feature Extraction |
|---|---|
| Creates new features using existing information. | Produces a new representation of the original data. |
| Often uses domain knowledge or mathematical operations. | Often uses statistical methods or learned representations. |
| Example: `price × quantity = total_amount` | Example: PCA transforms correlated features into principal components. |

**Remember:** Construction creates useful features; extraction transforms data into useful representations.

---

## 4. Quick Revision

| Type | Main Question | Example |
|---|---|---|
| Transformation | How can I improve an existing feature? | Scaling, imputation |
| Construction | Can I create a more useful feature? | Price × quantity |
| Selection | Which features should I keep? | RFE, Lasso |
| Extraction | Can I obtain a useful representation? | PCA, CNN |

### The Big Picture

Feature engineering helps convert raw data into information that Machine Learning models can use more effectively.

**Raw Data → Transform / Construct / Select / Extract → Model-Ready Features → ML Model**