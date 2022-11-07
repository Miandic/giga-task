import React from 'react';
import Header from './board/header';
import Board from './board/board'
import { Provider } from 'react-redux'
import store from './store/store'

function App() {
  return (
    <Provider store={store}>
      <div className='wrapper'>
        <Header />
        <Board />
      </div>
    </Provider>
  );
}

export default App;
