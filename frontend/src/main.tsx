import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'

import Home from './pages/Home'
import Login from './pages/Login/Login'
import ProfessorHome from './pages/ProfessorHome/ProfessorHome'
import TelaNotasProfessor from './pages/TelaNotasProfessor/TelaNotasProfessor'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/professor" element={<ProfessorHome />} />
        <Route path="/professor/nota-aluno" element={<TelaNotasProfessor />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>
)