import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import "./Login.css";

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setIsLoading(true);

    try {
      // Создаем FormData для отправки данных в формате application/x-www-form-urlencoded
      const formDataToSend = new URLSearchParams();
      formDataToSend.append("username", formData.username);
      formDataToSend.append("password", formData.password);

      const response = await fetch("http://localhost:8000/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        //body: formDataToSend,
        body:'grant_type=password&username=y&password=123&scope=&client_id=string&client_secret=string'
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Ошибка при входе");
      }
      console.log(data, "data");
      // Используем функцию login из AuthContext
      login(data.access_token);
      
      // Перенаправляем на главную страницу
      navigate("/dashboard");
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-container">
      <form className="login-box" onSubmit={handleSubmit}>
        <div className="login-title">Аналитика рекламных кампаний</div>
        {error && <div className="error-message">{error}</div>}
        <div className="login-label">Логин/Email</div>
        <div className="input-group">
          <i className="fa fa-envelope"></i>
          <input
            type="text"
            name="username"
            placeholder="Введите ваш логин"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="login-label">Пароль</div>
        <div className="input-group">
          <i className="fa fa-lock"></i>
          <input
            type={showPassword ? "text" : "password"}
            name="password"
            placeholder="Пароль"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <i
            className={showPassword ? "fa fa-eye-slash" : "fa fa-eye"}
            onClick={() => setShowPassword((v) => !v)}
            style={{ cursor: "pointer", marginLeft: "auto" }}
            title={showPassword ? "Скрыть пароль" : "Показать пароль"}
          ></i>
        </div>
        <button 
          className="login-btn" 
          type="submit"
          disabled={isLoading}
        >
          {isLoading ? "Вход..." : "Войти"}
        </button>
        <div className="login-links">
          <a href="/register">Зарегистрироваться</a>
        </div>
      </form>
    </div>
  );
}

export default Login; 