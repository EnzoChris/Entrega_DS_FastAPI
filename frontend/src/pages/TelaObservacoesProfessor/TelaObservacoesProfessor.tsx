import { useState } from 'react'
import { useNavigate, useParams, Link } from 'react-router-dom'
import ProfessorHeader from '../../components/ProfessorHeader/ProfessorHeader'
import CardObservacao from '../../components/CardObservacao/CardObservacao'
import BoxNovaObservacao from '../../components/BoxNovaObservacao/BoxNovaObservacao'
import styles from './TelaObservacoesProfessor.module.css'

// Placeholders — substituir pelos dados vindos da API
const professor = {
  nome: '/* NOME_PROFESSOR */',
  materias: '/* MATERIAS_PROFESSOR */',
  fotoPerfil: '/* URL_FOTO_PERFIL */',
}

const aluno = {
  nome: '/* NOME_ALUNO */',
  matricula: '/* MATRICULA_ALUNO */',
}

interface Observacao {
  titulo: string
  texto: string
  data: string
}

const observacoesIniciais: Observacao[] = [] /* OBSERVACOES_ALUNO */

export default function TelaObservacoesProfessor() {
  const navigate = useNavigate()
  const { matricula } = useParams() /* MATRICULA via React Router */

  const [mostrarBox, setMostrarBox] = useState(false)
  const [observacoes, setObservacoes] = useState<Observacao[]>(observacoesIniciais)

  function handleEnviar(texto: string) {
    /* CHAMADA_API_ADICIONAR_OBSERVACAO */
    setObservacoes([...observacoes, {
      titulo: 'Nova observação',
      texto,
      data: new Date().toLocaleDateString('pt-BR'),
    }])
    setMostrarBox(false)
  }

  return (
    <>
      <ProfessorHeader
        nomeProfessor={professor.nome}
        materias={professor.materias}
        fotoPerfil={professor.fotoPerfil}
      />
      <main>
        <button className={styles.btnVoltar} onClick={() => navigate(-1)}>
          <i className="bi bi-arrow-left-circle"></i>
          <p>Voltar</p>
        </button>

        <div className={styles.blocoAluno}>
          <div className={styles.iconeUser}>
            <i className="bi bi-person"></i>
          </div>
          <div>
            <h2>{aluno.nome}</h2>
            <p>Matrícula: {aluno.matricula}</p>
          </div>
        </div>

        <div className={styles.options}>
          <Link to={`/professor/aluno/${matricula}/notas`} className={styles.abaNotas}>
            <i className="bi bi-journal"></i>
            <p>Notas</p>
          </Link>
          <div className={styles.abaObservacoes}>
            <i className="bi bi-chat-left-dots"></i>
            <p>Observações</p>
          </div>
        </div>

        <div className={styles.preObservacoes}>
          <div className={styles.tituloComContador}>
            <h2>Observações</h2>
            <span className={styles.contadorObs}>{observacoes.length}</span>
          </div>
          <button className={styles.btnAdicionarObservacao} onClick={() => setMostrarBox(!mostrarBox)}>
            <i className="bi bi-plus"></i>
            <p>Adicionar Observação</p>
          </button>
        </div>

        {mostrarBox && (
          <BoxNovaObservacao
            onCancelar={() => setMostrarBox(false)}
            onEnviar={handleEnviar}
          />
        )}

        <div className={styles.containerObservacoes}>
          {observacoes.map((obs, i) => (
            <CardObservacao key={i} titulo={obs.titulo} texto={obs.texto} data={obs.data} />
          ))}
        </div>
      </main>
    </>
  )
}