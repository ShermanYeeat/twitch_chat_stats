import React , {useState, useEffect} from 'react';
// import TwitchUsers from './TwitchUsers';


  /*
  const urlRef = useRef()
  function getTopUsersandEmotes(e) {
    const url = urlRef.current.value
    if (url == '') return
    console.log(url)
    urlRef.current.value = null
  }

 return (
   <>
    <TwitchUsers />
    <input ref={urlRef} type="text" />
    <button onClick={getTopUsersandEmotes}>Enter</button>
   </>
 )
 */
function App() {
    const [data, setData] = useState([])
    const [data2, setData2] = useState([])

    useEffect(() => {
        fetch('/test')
        .then(response => response.json())
        .then(data => setData(data))
    }, []);

    
    useEffect(() => {
        fetch('/test2')
        .then(response => response.json())
        .then(data2 => setData2(data2))
    }, []);
    

    return (
        <>
        <div className="container">
            <h2>Top Users</h2>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>User</th>
                        <th># of Messages</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        data.map((item, i) => (
                            <tr key={item.user}>
                                <td>{i + 1}</td>
                                <td>{item.user}</td>
                                <td>{item.messages}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>

        <div className="container">
            <h2>Top Emotes</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Emote</th>
                            <th>Times Used</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            data2.map(({emote, messages}, i) => (
                                <tr key={emote}>
                                    <td>{i + 1}</td>
                                    <td>{asd(emote)}</td>
                                    <td>{messages}</td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
        </div>
        </>

    )
}

function asd(value) {
    if (value === 'Clap' || value === 'gachiBASS' || value === 'pepeD' || value === 'pepeJAM') return <img src={require(`./gifs/${value}.gif`)}/>
    return <img src={require(`./images/${value}.png`)}/>
}






export default App;
