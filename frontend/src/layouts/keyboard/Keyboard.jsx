export default function Keyboard() {
  return(
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
