import { useState } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Question from './components/Questions'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
            <Routes>
                <Route path="/" element={<Question />} />
            </Routes>
        </Router>
  )
}

export default App
