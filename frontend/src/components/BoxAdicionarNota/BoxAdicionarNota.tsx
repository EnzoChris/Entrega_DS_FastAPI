import { useState } from 'react'
import styles from './BoxAdicionarNota.module.css'

interface Disciplina {
  codigo: string
  nome: string
}

interface Props {
  matriculaAluno: string        /* MATRICULA_ALUNO */
  usuarioProfessor: string      /* USUARIO_PROFESSOR */
  disciplinas: Disciplina[]     /* DISCIPLINAS_PROFESSOR */
  onCancelar: () => void
  onSalvar: (dados: { n1: number; n2: number; codigoDisciplina: string }) => void
}

export default function BoxAdicionarNota({ matriculaAluno, usuarioProfessor, disciplinas, onCancelar, onSalvar }: Props) {
  const [n1, setN1] = useState('')
  const [n2, setN2] = useState('')
  const [codigoDisciplina, setCodigoDisciplina] = useState('')

  function handleSalvar() {
    onSalvar({ n1: Number(n1), n2: Number(n2), codigoDisciplina })
  }

  return (
    <div className={styles.box}>
      <h3>Lançamento de Nota</h3>

      <div className={styles.inputsNota}>
        <input
          type="number" step=".01" min="0" max="10"
          placeholder="Digite a n1"
          value={n1}
          onChange={(e) => setN1(e.target.value)}
        />
        <input
          type="number" step=".01" min="0" max="10"
          placeholder="Digite a n2"
          value={n2}
          onChange={(e) => setN2(e.target.value)}
        />
        <select value={codigoDisciplina} onChange={(e) => setCodigoDisciplina(e.target.value)}>
          <option value="">-- Selecione --</option>
          {disciplinas.map((d) => (
            <option key={d.codigo} value={d.codigo}>{d.nome}</option>
          ))}
        </select>
      </div>

      <div className={styles.botoesNota}>
        <button className={styles.cancelar} onClick={onCancelar}>Cancelar</button>
        <button className={styles.salvar} onClick={handleSalvar}>Concluir</button>
      </div>
    </div>
  )
}