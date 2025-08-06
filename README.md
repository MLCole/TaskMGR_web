# 📝 TaskMGR\_web

**TaskMGR\_web** is a minimalist, Streamlit-powered web application designed to help you manage your daily tasks and to-dos efficiently. It reads and writes to a plain text file (`todos.txt`), keeping your task list simple, accessible, and editable even outside the app.

---

## 🚀 Features

* ✅ Add, complete, and remove tasks via the browser.
* 🔄 Automatic syncing with a plain-text task list.
* 📁 Simple backend logic stored in `functions.py`.
* 📦 Built with [Streamlit](https://streamlit.io/) for rapid UI deployment.

---

## 📂 Project Structure

```
TaskMGR_web/
├── functions.py         # Backend logic for reading and writing tasks
├── web_frontend.py      # Streamlit web app interface
├── todos.txt            # Your persistent task list (plain text)
└── requirements.txt     # All Python dependencies
```

---

## 🛠️ Installation

1. Clone the repo:

```bash
git clone https://github.com/MLCole/TaskMGR_web.git
cd TaskMGR_web
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the web app locally:

```bash
streamlit run web_frontend.py
```

The app will open in your default browser. You can:

* View all current tasks.
* Add new ones using the input box.
* Check off tasks to remove them from the list.
* Click "Clear Completed Tasks" to reload the UI after changes.

---

## 💡 Example ToDos

Located in `todos.txt`, your current list might look like:

```
Alien watchout
Learn
Confirm it works
And me too!
```

---

## 📌 Notes

* The task list is stored in `todos.txt` and is **persistent** across runs.
* Tasks are saved in plain text — easy to back up or modify outside the app.
* Designed to be portable and beginner-friendly for learning purposes.

---

## 👌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📄 License

MIT License — feel free to use, modify, and share!
