package queue

// Queue mock queue
type Queue struct {
	store []int
}

func (q *Queue) Enqueue(val int) {
	if q.store == nil {
		q.store = []int{val}
		return
	}

	q.store = append(q.store, val)
}

func (q *Queue) Dequeue() (int, bool) {
	if q.store == nil || len(q.store) == 0 {
		return -1, false
	}
	ret := q.store[0]
	q.store = q.store[1:]
	return ret, true
}
