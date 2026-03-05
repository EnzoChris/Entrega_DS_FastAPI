import styles from './NotaCard.module.css'

interface Props {
  index: number
  disciplina: string
  n1: number
  n2: number
  media: number
}

export default function NotaCard({ index, disciplina, n1, n2, media }: Props) {
  return (
    <div className={styles.notaCard}>
      <p>{index}ª Nota - {disciplina}</p>
      <div className={styles.editGradeAndGrade}>
        <p className={styles.valorNota}>N1: {n1}</p>
        <p className={styles.valorNota}>N2: {n2}</p>
        <p className={styles.valorNota}>Média: {media}</p>
      </div>
    </div>
  )
}