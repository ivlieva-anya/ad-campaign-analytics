import React from "react";
import { useNavigate } from "react-router-dom";
import "./Reports.css";

function Reports() {
  const navigate = useNavigate();
  return (
    <div className="reports-root">
      <aside className="reports-sidebar">
        <div className="sidebar-title">Меню</div>
        <nav className="sidebar-nav">
          <a href="#" className="sidebar-link" onClick={e => {e.preventDefault(); navigate('/profile');}}>Профиль</a>
          <a href="#" className="sidebar-link active">Мои отчёты</a>
          <a href="#" className="sidebar-link" onClick={e => {e.preventDefault(); navigate('/dashboard');}}>Главная</a>
        </nav>
      </aside>
      <main className="reports-main">
        <div className="reports-header">
          <h1>Мои отчёты</h1>
          <span className="reports-warning">Отчеты хранятся 7 дней</span>
          <button className="reports-new-btn" onClick={() => navigate('/report-wizard')}>+ Новый отчёт</button>
        </div>
        <div className="reports-filters">
          <div className="reports-sort">
            Сортировка:
            <input type="text" className="reports-sort-input" />
          </div>
          <div className="reports-search">
            <input type="text" className="reports-search-input" placeholder="Поиск по названию" />
            <span className="reports-search-toggle">on</span>
            <span className="reports-search-label">Только активные</span>
          </div>
        </div>
        <div className="reports-list">
          <div className="report-card">
            <div className="report-title">Анализ кампании Nike — <b>12.05</b></div>
            <div className="report-progress">
              <div className="progress-bar">
                <div className="progress-bar-inner" style={{width: '80%'}}></div>
              </div>
              <span className="report-delete">Удалится через 2 дня (15.05)</span>
            </div>
            <div className="report-format">
              <i className="fa fa-file-pdf"></i> Формат: PDF
            </div>
            <div className="report-actions">
              <button className="report-download">Скачать</button>
              <button className="report-archive" disabled>Архивировать</button>
              <button className="report-trash"><i className="fa fa-trash"></i></button>
            </div>
          </div>
        </div>
        <div className="reports-empty">
          <div className="empty-icon"><i className="fa fa-inbox"></i></div>
          <div className="empty-text">Здесь появятся ваши отчеты</div>
          <button className="empty-create-btn">Создать первый отчет</button>
        </div>
      </main>
    </div>
  );
}

export default Reports; 