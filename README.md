```markdown
# CareerBuddyPro

ระบบติดตามสมัครงานอัจฉริยะ พร้อมฟีเจอร์วิเคราะห์ Skill Gap และ Reminder

---

## โครงสร้างโปรเจกต์

- **backend/**: FastAPI + SQLModel  
- **frontend/**: Vue.js + Tailwind CSS  

---

## วิธีใช้งานเบื้องต้น

1. **สร้างและเปิดใช้งาน virtual environment**  
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **ติดตั้ง dependencies (backend + frontend)**  
   ```bash
   # ติดตั้ง backend dependencies
   pip install -r requirements.txt

   # เข้าโฟลเดอร์ frontend และติดตั้ง
   cd frontend
   npm install
   ```

3. **รันเซิร์ฟเวอร์ backend**  
   ```bash
   # กลับไปที่โฟลเดอร์ backend (ถ้าอยู่ใน frontend)
   cd ..

   uvicorn app.main:app --reload
   ```
   _โดยค่าเริ่มต้น FastAPI จะรันที่_ `http://127.0.0.1:8000`

4. **รันแอปพลิเคชัน frontend**  
   ```bash
   cd frontend
   npm run serve
   ```
   _โดยค่าเริ่มต้น Vue.js จะรันที่_ `http://localhost:8080`

---

## คำแนะนำเพิ่มเติม

- เก็บค่า configuration ทั้งหมดในไฟล์ `.env` (ดูตัวอย่างใน `.env.example`)  
- อย่าลืมเพิ่มไฟล์สำคัญลงใน `.gitignore` เช่น `.venv/`, `node_modules/`, `*.pyc`  
- รัน Unit Tests ด้วย  
  ```bash
  pytest
  ```
```

