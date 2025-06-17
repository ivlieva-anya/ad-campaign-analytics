import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Register.css";

function Register() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [error, setError] = useState("");

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

    if (formData.password !== formData.confirmPassword) {
      setError("Пароли не совпадают");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/api/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Ошибка при регистрации");
      }

      // После успешной регистрации перенаправляем на страницу входа
      console.log();
      navigate("/login");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <form className="register-box" onSubmit={handleSubmit}>
        <h2>Регистрация</h2>
        {error && <div className="error-message">{error}</div>}
        <div className="input-group">
          <i className="fa fa-user"></i>
          <input
            type="text"
            name="username"
            placeholder="Логин"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <i className="fa fa-envelope"></i>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <i className="fa fa-lock"></i>
          <input
            type="password"
            name="password"
            placeholder="Пароль"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <i className="fa fa-lock"></i>
          <input
            type="password"
            name="confirmPassword"
            placeholder="Подтвердите пароль"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />
        </div>
        <button className="register-btn" type="submit">
          Зарегистрироваться
        </button>
        <div className="login-link">
          Уже есть аккаунт?
          <a href="/login">Войти</a>
        </div>
      </form>
    </div>
  );
}

export default Register; 