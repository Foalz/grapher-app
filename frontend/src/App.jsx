import { useState, useEffect } from 'react'
import axios from 'axios'
import Bokeh from '@bokeh/bokehjs/build/js/bokeh.esm.min.js';
import { Button } from '@mui/material';
import { addStyles, EditableMathField, } from "react-mathquill";

addStyles();

function App() {
  const [latex, setLatex] = useState('');
  async function getPlotData() {
    const response = await axios.post(`http://127.0.0.1:8000/api/plot`, {
      latex_string: latex 
    });
    const myNode = document.getElementById("bokeh");
    myNode.replaceChildren(); // clean previous plot
    Bokeh.embed.embed_item(response.data, 'bokeh')
  }
  return (
    <>
      <EditableMathField 
        latex={latex}
        onChange={(mathField) => {
        setLatex(mathField.latex())
        }}
      />
      <div id='bokeh' className="bk-root"></div>
      <Button onClick={e => getPlotData()}>TEST</Button>
    </>
  )
}

export default App
