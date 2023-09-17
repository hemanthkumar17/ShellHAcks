import axios from "axios";
import { useState, useEffect } from "react";

const path = "http://127.0.0.1:5000";
import React from "react";
// import YoutubeEmbed from "react-youtube-embed";

function Learn(){
    const [report, setReport] = useState([]);
    const [vidIds, setVidIds] = useState([]);
    const options = {
        height: '390',
        width: '640',
        playerVars: {
          autoplay: 1,
          controls: 1,
        },
      };
    useEffect(() => {
    async function getReport() {
      const response = await axios.get(`${path}/report`, {}, {});
      console.log(response.data.topics[0][0]);
      setReport(response.data.topics[0][0]);
    }

    
    async function getVideos() {
        const response = await axios.get(`${path}/videos`, {}, {});
        console.log(response.data);
        console.log(response.data.ids);
        setVidIds(response.data);
      }
    getReport();
    getVideos();
    }, []);
    return (<div>
      {vidIds.ids?.map((videoId) => (
        <iframe 
        sandbox='allow-same-origin allow-forms allow-popups allow-scripts allow-presentation'
        frameborder='10 | 10'
        allow='autoplay; encrypted-media'
        allowFullScreen
        src={`https://www.youtube.com/embed/${videoId}`}></iframe>
      ))} 
    </div>);
};

export default Learn;