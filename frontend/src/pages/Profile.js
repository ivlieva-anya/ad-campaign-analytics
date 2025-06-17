import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Profile.css";

function Profile() {
  const [editMode, setEditMode] = useState(false);
  const [form, setForm] = useState({
    firstName: "Имя",
    lastName: "Фамилия",
    email: "email@example.com",
    avatar: null,
    avatarPreview: null,
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === "avatar" && files && files[0]) {
      setForm((prev) => ({
        ...prev,
        avatar: files[0],
        avatarPreview: URL.createObjectURL(files[0]),
      }));
    } else {
      setForm((prev) => ({ ...prev, [name]: value }));
    }
  };

  const handleEdit = () => setEditMode(true);
  const handleCancel = () => setEditMode(false);
  const handleSave = (e) => {
    e.preventDefault();
    setEditMode(false);
    // Здесь можно добавить сохранение на сервер
  };

  return (
    <div className="profile-root">
      <aside className="profile-sidebar">
        <div className="sidebar-title">Меню</div>
        <nav className="sidebar-nav">
          <a href="#" className="sidebar-link active">Профиль</a>
          <a href="/reports" className="sidebar-link">Мои отчеты</a>
          <a href="#" className="sidebar-link" onClick={e => {e.preventDefault(); navigate('/dashboard');}}>Главная</a>
        </nav>
        <a href="#" className="sidebar-exit" onClick={e => {e.preventDefault(); navigate('/login');}}>Выйти</a>
      </aside>
      <main className="profile-main">
        <h1>Личный кабинет</h1>
        <div className="profile-card">
          <div className="profile-avatar">
            {form.avatarPreview ? (
              <img src={form.avatarPreview} alt="avatar" className="avatar-img" />
            ) : (
              <div className="avatar-placeholder">100 × 100</div>
            )}
          </div>
          <div className="profile-info">
            {editMode ? (
              <form className="profile-edit-form" onSubmit={handleSave}>
                <input
                  className="profile-input"
                  type="text"
                  name="firstName"
                  value={form.firstName}
                  onChange={handleChange}
                  placeholder="Имя"
                  required
                />
                <input
                  className="profile-input"
                  type="text"
                  name="lastName"
                  value={form.lastName}
                  onChange={handleChange}
                  placeholder="Фамилия"
                  required
                />
                <input
                  className="profile-input"
                  type="email"
                  name="email"
                  value={form.email}
                  onChange={handleChange}
                  placeholder="Почта"
                  required
                />
                <input
                  className="profile-input"
                  type="file"
                  name="avatar"
                  accept="image/*"
                  onChange={handleChange}
                />
                <div className="profile-edit-actions">
                  <button type="submit" className="profile-edit-btn">Сохранить</button>
                  <button type="button" className="profile-cancel-btn" onClick={handleCancel}>Отмена</button>
                </div>
              </form>
            ) : (
              <>
                <div className="profile-name">{form.firstName} {form.lastName}</div>
                <div className="profile-email">{form.email}</div>
                <div className="profile-date">Дата регистрации: 01.01.2024</div>
                <button className="profile-edit-btn" onClick={handleEdit}>Редактировать</button>
              </>
            )}
          </div>
        </div>
        <div className="profile-stats">
          <div className="stat-card">
            <i className="fa fa-chart-bar"></i>
            <div className="stat-label">Всего отчетов</div>
            <div className="stat-value">25</div>
          </div>
          <div className="stat-card">
            <i className="fa fa-search"></i>
            <div className="stat-label">Последний запрос</div>
            <div className="stat-value">01.01.2024</div>
          </div>
          <div className="stat-card">
            <i className="fa fa-star"></i>
            <div className="stat-label">Избранные источники</div>
            <div className="stat-socials">
              <i className="fa fa-twitter"></i>
              <i className="fa fa-facebook"></i>
              <i className="fa fa-instagram"></i>
            </div>
          </div>
        </div>
        <div className="profile-actions">
          <div className="actions-title">Быстрые действия</div>
          <button className="change-password-btn">Изменить пароль</button>
        </div>
        <div className="profile-bell">
          <i className="fa fa-bell"></i>
        </div>
      </main>
    </div>
  );
}

export default Profile; 