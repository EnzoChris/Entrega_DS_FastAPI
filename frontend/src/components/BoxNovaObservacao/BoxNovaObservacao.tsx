import { useState } from 'react'
import styles from './BoxNovaObservacao.module.css'

interface Props {
  onCancelar: () => void
  onEnviar: (texto: string) => void
}

export default function BoxNovaObservacao({ onCancelar, onEnviar }: Props) {
  const [texto, setTexto] = useState('')

  function handleEnviar() {
    onEnviar(texto)
    setTexto('')
  }

  return (
    <div className={styles.box}>
      <h4>Nova observação</h4>
      <textarea
        placeholder="Digite sua observação..."
        value={texto}
        onChange={(e) => setTexto(e.target.value)}
      />
      <div className={styles.botoesComentario}>
        <button className={styles.cancelar} onClick={onCancelar}>Cancelar</button>
        <button className={styles.enviar} onClick={handleEnviar}>Enviar</button>
      </div>
    </div>
  )
}