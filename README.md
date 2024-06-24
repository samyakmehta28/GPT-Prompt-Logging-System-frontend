<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">PROMPTLOGGINGSYSTEM-FRONTEND</h1>
</p>
<p align="center">
    <em>Log smarter, prompt faster: Peak logging efficiency!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/samyakmehta28/PromptLoggingSystem-frontend?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/samyakmehta28/PromptLoggingSystem-frontend?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/samyakmehta28/PromptLoggingSystem-frontend?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/samyakmehta28/PromptLoggingSystem-frontend?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat&logo=Plotly&logoColor=white" alt="Plotly">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running PromptLoggingSystem-frontend](#-running-PromptLoggingSystem-frontend)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The PromptLoggingSystem-frontend project is a Streamlit-based application designed to provide a user-friendly interface for querying an API and generating responses based on user input. It boasts features like performance metric calculations, dynamic dashboards with filtering capabilities for data visualization, and interactive data analysis options. By structuring requests, handling responses, and filtering data from the backend API, it offers a seamless experience for monitoring and analyzing prompt logging activities, ultimately enhancing efficiency and decision-making processes.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | This project has a modular architecture using Streamlit for interactive data analysis and visualization. It integrates components for querying APIs, handling responses, and generating metrics. |
| 🔩 | **Code Quality**  | The codebase maintains a consistent style with clear structure and naming conventions. It adheres to PEP 8 guidelines, enhancing readability and maintainability. |
| 📄 | **Documentation** | The project includes inline documentation for functions and classes. However, there is room for improvement in providing comprehensive external documentation for setup, usage, and contributing guidelines. |
| 🔌 | **Integrations**  | Key integrations include Streamlit for the interactive dashboard, GitPython for version control operations, and various libraries for data processing and visualization such as pandas, plotly, and altair. |
| 🧩 | **Modularity**    | The project exhibits good modularity with distinct components for querying APIs, generating metrics, and visualizing data. This promotes code reusability and extensibility. |
| 🧪 | **Testing**       | Testing frameworks and tools utilized in the project are not explicitly mentioned in the repository details. It would be beneficial to include testing frameworks like pytest for ensuring code reliability. |
| ⚡️  | **Performance**   | The efficiency and performance of the project rely on the underlying technologies such as Streamlit for dynamic data visualization and Tornado for handling web requests, ensuring responsiveness and resource optimization. |
| 🛡️ | **Security**      | Security measures such as data protection and access control implementations are not explicitly mentioned in the repository details. Incorporating authentication mechanisms and data encryption can enhance security. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include pandas, plotly, requests, GitPython, and Streamlit for data processing, visualization, API handling, and building interactive dashboards. |
| 🚀 | **Scalability**   | The project's scalability is supported by Streamlit's ability to handle increased traffic and load when serving dynamic dashboards and visualizations, ensuring responsiveness under varying user loads. |


---

##  Repository Structure

```sh
└── PromptLoggingSystem-frontend/
    ├── README.md
    ├── pages
    │   ├── Dashboard.py
    │   └── Metrics.py
    ├── prompt.py
    └── requirements.txt
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                           | Summary                                                                                                                                                                                      |
| ---                                                                                                            | ---                                                                                                                                                                                          |
| [prompt.py](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/blob/master/prompt.py)               | The code in prompt.py enables querying an API for response generation based on user input. It structures requests and handles responses within the Streamlit app for the Response Generator. |
| [requirements.txt](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/blob/master/requirements.txt) | Code snippet in `Metrics.py` calculates and displays performance metrics for the logging system dashboard in `PromptLoggingSystem-frontend`.                                                 |

</details>

<details closed><summary>pages</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                               |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                   |
| [Metrics.py](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/blob/master/pages/Metrics.py)     | Summary: `Metrics.py` in PromptLoggingSystem-frontend retrieves and filters data from the backend API, generating metrics like total tokens and requests per second for a dynamic Streamlit dashboard.                                                |
| [Dashboard.py](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/blob/master/pages/Dashboard.py) | Dashboard Filtering & Data Visualization**Dashboard.py file queries and filters backend API data for prompt logging system. Provides interactive data analysis using Streamlit with filtering options for time, environment, model, status, and user. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the PromptLoggingSystem-frontend repository:

```sh
git clone https://github.com/samyakmehta28/PromptLoggingSystem-frontend
```

2. Change to the project directory:

```sh
cd PromptLoggingSystem-frontend
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running PromptLoggingSystem-frontend

Use the following command to run PromptLoggingSystem-frontend:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/samyakmehta28/PromptLoggingSystem-frontend/issues)**: Submit bugs found or log feature requests for Promptloggingsystem-frontend.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/samyakmehta28/PromptLoggingSystem-frontend
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
