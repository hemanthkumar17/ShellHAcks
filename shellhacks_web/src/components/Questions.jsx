import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useEffect } from "react";
import { Loading } from "./Loading";
import { BASE_URL } from "../config";

function Question() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    async function getQuestions() {
      const response = await axios.get(`${BASE_URL}/questions`, {}, {});
      setQuestions(response.data);
    }

    getQuestions();
  }, []);

  return (
    <div>
      <h1>Take the QUIZ!</h1>
      <QuestionCard questions={questions} />
      {/* <BottomNav/> */}
    </div>
  );
}

function QuestionCard({ questions }) {
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  
  return (
    <div className="question">
      <div className="card-container">
        {questions.length > 0 ? (
          <QuestionItem
            question={questions}
            index={currentCardIndex}
            changeIndex={setCurrentCardIndex}
          ></QuestionItem>
        ) : (
          <Loading />
        )}

        {/* {questions && (
          <QuestionItem
            question={questions}
            index={currentCardIndex}
          ></QuestionItem>
        )} */}
      </div>
      {/* {<SubmitQuiz index={currentCardIndex} />} */}
    </div>
  );
}

function QuestionItem(props) {
  const [answers, setAnswers] = useState([]);
  const [answer, setAnswer] = useState("");

  const handleNextCard = () => {
    // setCurrentCardIndex((prevIndex) => (prevIndex + 1) % cardsData.length);
    if (answer.length > 0) {
      setAnswers([...answers, answer]);
      setAnswer("");
      props.changeIndex(props.index + 1);
    }
  };

  const handlePrevCard = () => {
    // setCurrentCardIndex((prevIndex) =>
    // prevIndex === 0 ? cardsData.length - 1 : prevIndex - 1);
    props.changeIndex(props.index - 1);
  };

  return (
    <div className="questions_container">
      {/* <button className="nav-button prev" onClick={handlePrevCard}>
        &lt;
      </button> */}
      <div className="row_container">
        {props.index === 0 ? (
          <></>
        ) : (
          <button className="nav-button prev" onClick={handlePrevCard}>
            &lt;
          </button>
        )}
        <Card sx={{ maxWidth: 345 }}>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              {props.question[props.index].question}
            </Typography>

            <TextField
              id="outlined-basic"
              label="Type your answer here"
              variant="outlined"
              onChange={(e) => {
                setAnswer(e.target.value);
              }}
            />
          </CardContent>
        </Card>
        {props.index === props.question.length - 1 ? (
          <></>
        ) : (
          <button className="nav-button next" onClick={handleNextCard}>
            &gt;
          </button>
        )}
      </div>

      {props.index === props.question.length - 1 ? (
        <SubmitQuiz answers={answers} questions={props.question} />
      ) : (
        <></>
      )}
    </div>
  );
}

function SubmitQuiz({ answers, questions }) {
  const navigate = useNavigate("");
  const [load, setLoad] = useState()
  return (
    <div className="submit-btn">
      <Button
        variant="contained"
        onClick={async () => {
          setLoad(true);
          const response = await axios.post(
            `${BASE_URL}/answers`,
            {
              answers: answers,
              qa_pairs: questions,
            },
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          );
          setLoad(false);
          if (response.status != 200) {
            throw new Error("Request failed");
          } else {
            navigate("/answers");
          }
        }}
      >
        SUBMIT
      </Button>
      {/* {load === true ? <Loading /> : null} */}
    </div>
  );
}

export default Question;
