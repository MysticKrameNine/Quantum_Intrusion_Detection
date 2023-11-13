# Quantum Machine Learning Intrusion Detection System

## Running the code
Run the Jupyter Notebooks using your virtual environment (venv) as kernel.

### How to create your virtual environment
```bash
python -m venv ./venv
```

### How to temporary activate your virtual environment in your terminal
#### Windows PowerShell
```bash
.\venv\Scripts\Activate.ps1
```

#### Linux / MacOS
```bash
source ./venv/bin/activate
```

#### If error of security policy occurs
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

### How to install the required packages
```bash
pip install -r requirements.txt
```

### How to add your virtual environment to Jupyter
```bash
python -m ipykernel install --user --name=venv
```

### How to run Jupyter Notebooks (you need to select your virtual environment as kernel)
```bash
jupyter notebook
```

## Information
[Getting started](https://qiskit.org/documentation/getting_started.html)

[Machine learning](https://qiskit.org/ecosystem/machine-learning/getting_started.html)

### Dataset used
NSL-KDD

### QML Algorithms used
QSVM: Quantum Support Vector Machine

### Results

## How to install the required packages instead of using the requirements.txt file

### Install Qiskit
pip install qiskit

### Install Qiskit Visualization for Jupyter
pip install qiskit[visualization]

### Install Qiskit Machine Learning
pip install qiskit[machine-learning]

### Install Sklearn (to use dataset)
pip install scikit-learn

### Install ipykernel (to use the virtual environment in Jupyter)
pip install ipykernel

### Add the virtual environment to Jupyter
python -m ipykernel install --user --name=venv

## Subject
Keywords: Quantum machine learning, data driven security, intrusion detection systems, NSL-KDD.
Synopsis:
Several traditional machine learning based intrusion detection systems approaches showed high accu- racy in detecting and classifying network intrusions. However, the performance of training these mod- els degrades as the training dataset increases in size.
Quantum machine learning (QML) has attracted the attention of the scientific community as an alterna- tive to traditional machine learning to alleviate performance issues.
The objective of this research is to explore the use of QML to driven data security and to implement ef- ficient intrusion detection systems.
Advising modality:
Contact the advisor to schedule a meeting as soon as you choose to work on this subject.
Deliverable:
•
Research report: Title, abstract, introduction, state of the art, research methodology, results, conclusion, references.
Presentation pptx.
• Code.
Academic integrity:
It is very important to correctly acknowledge any ideas, code, or written works by others. Any plagiarism will receive a zero grade.
Bibliography:
Kalinin, M., Krundyshev, V. Security intrusion detection using quantum machine leaming techniques. J Comput Virol Hack Tech 19, 125-136 (2023). https://doi.org/10.1007/s11416-022-00435-0

![3-quantummachi](https://github.com/ikramebakkari/Quantum_Intrusion_Detection/assets/56300696/a91c7008-4ad7-4465-8966-f05a2315c69d)