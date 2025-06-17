import React from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";

function Dashboard() {
  const navigate = useNavigate();
  return (
    <div className="dashboard-root dashboard-double-sidebar">
      <aside className="profile-sidebar dashboard-menu-sidebar">
        <div className="sidebar-title">Меню</div>
        <nav className="sidebar-nav">
          <a href="/profile" className="sidebar-link" onClick={e => {e.preventDefault(); navigate('/profile');}}>Профиль</a>
          <a href="/reports" className="sidebar-link" onClick={e => {e.preventDefault(); navigate('/reports');}}>Мои отчёты</a>
          <a href="/dashboard" className="sidebar-link active">Главная</a>
        </nav>
      </aside>
      <aside className="dashboard-sidebar">
        <h2>Мониторинг упоминаний</h2>
        <div className="sidebar-label">Выбор источника</div>
        <input className="sidebar-input" type="text" />
        <div className="sidebar-label">Название продукта</div>
        <input className="sidebar-input" type="text" placeholder="Введите название продукта" />
        <button className="sidebar-btn">Анализировать</button>
        <div className="sidebar-label">Диапазон дат</div>
        <input className="sidebar-input" type="text" />
        <input className="sidebar-input" type="text" />
        <div className="sidebar-label">Тональность</div>
        <input className="sidebar-input" type="text" />
      </aside>
      <main className="dashboard-main">
        <h1>Результаты анализа</h1>
        <div className="dashboard-cards">
          <div className="dashboard-card">
            <div className="card-title"><a href="#">Название статьи 1</a></div>
            <div className="card-site">Сайт</div>
            <div className="card-date">Дата публикации:</div>
            <div className="card-mentions">Упоминаний: <span className="card-mentions-count">150</span></div>
            <div className="card-tone card-tone-positive">Позитивная</div>
            <div className="card-summary">Краткая выдержка: Это ключевое предложение с упоминанием продукта.</div>
            <div className="card-graph">[График динамики упоминаний]</div>
          </div>
          <div className="dashboard-card">
            <div className="card-title"><a href="#">Название статьи 2</a></div>
            <div className="card-site">Сайт</div>
            <div className="card-date">Дата публикации:</div>
            <div className="card-mentions">Упоминаний: <span className="card-mentions-count card-mentions-negative">75</span></div>
            <div className="card-tone card-tone-negative">Негативная</div>
            <div className="card-summary">Краткая выдержка: Это еще одно ключевое предложение с упоминанием продукта.</div>
            <div className="card-graph">[График динамики упоминаний]</div>
          </div>
        </div>
        <div className="dashboard-tags-block">
          <div className="tags-title">Облако тегов</div>
          <div className="tags-list">
            <span className="tag">Тег</span>
            <span className="tag">Тег</span>
            <span className="tag">Тег</span>
            <span className="tag">Тег</span>
            <span className="tag">Тег</span>
          </div>
        </div>
        <button className="dashboard-create-btn" onClick={() => navigate('/report-wizard')}>Создать</button>
      </main>
    </div>
  );
}

export default Dashboard; 