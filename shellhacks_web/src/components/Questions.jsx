import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import Pagination from "@mui/material/Pagination";
import Stack from "@mui/material/Stack";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useEffect } from "react";
import { Loading } from "./Loading";

const path = "http://127.0.0.1:5000";

function Question() {
  const [cardClicked, setCardClicked] = useState(false);
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    async function getQuestions() {
      const response = await axios.get(`${path}/questions`, {}, {});
      // console.log(response.data);
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
  // console.log(props.questions);

  // questions.map((item) => {
  //   console.log(item.question);
  // });
  const [currentCardIndex, setCurrentCardIndex] = useState(0);

  const handleNextCard = () => {
    // setCurrentCardIndex((prevIndex) => (prevIndex + 1) % cardsData.length);
    setCurrentCardIndex(currentCardIndex + 1);
    console.log(currentCardIndex);
  };

  const handlePrevCard = () => {
    // setCurrentCardIndex((prevIndex) =>
    // prevIndex === 0 ? cardsData.length - 1 : prevIndex - 1);
    setCurrentCardIndex(currentCardIndex - 1);
    console.log(currentCardIndex);
  };

  return (
    <div className="question">
      <div className="card-container">
        <button className="nav-button prev" onClick={handlePrevCard}>
          &lt;
        </button>
        {/* {questions &&
          questions.map((item) => {
            return <QuestionItem question={item.question} />;
          })} */}

        {questions.length > 0 ? (
          <QuestionItem
            question={questions}
            index={currentCardIndex}
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
        <button className="nav-button next" onClick={handleNextCard}>
          &gt;
        </button>
      </div>
      {<SubmitQuiz index={currentCardIndex} />}
    </div>
  );
}

function QuestionItem(props) {
  console.log("ab", props.question);
  console.log("cd", props.index);
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {props.question[props.index].question}
          </Typography>
          {/* <Typography variant="body2" color="text.secondary">
              Lizards are a widespread group of squamate reptiles, with over 6,000
              species, ranging across all continents except Antarctica
          </Typography> */}
          <TextField
            id="outlined-basic"
            label="Type your answer here"
            variant="outlined"
          />
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

function SubmitQuiz({ index }) {
  const navigate = useNavigate("");
  if (index == 3) {
    return (
      <div className="submit-btn">
        <Button
          variant="contained"
          onClick={() => {
            navigate("/learn");
          }}
        >
          SUBMIT
        </Button>
      </div>
    );
  } else {
    return <></>;
  }
}

function BottomNav() {
  const [isCompleted, setIsCompleted] = useState(false);

  if (isCompleted) {
    return <Button variant="contained">SUBMIT</Button>;
  } else {
    return (
      <Stack spacing={2}>
        <Pagination count={6} size="large" color="primary" />
      </Stack>
    );
  }
}

export default Question;
