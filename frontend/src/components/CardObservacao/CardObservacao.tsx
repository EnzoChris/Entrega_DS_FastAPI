import styles from './CardObservacao.module.css'

interface Props {
  titulo: string
  texto: string
  data: string
}

export default function CardObservacao({ titulo, texto, data }: Props) {
  return (
    <div className={styles.card}>
      <h4>{titulo}</h4>
      <p>{texto}</p>
      <p className={styles.dataObs}>{data}</p>
    </div>
  )
}