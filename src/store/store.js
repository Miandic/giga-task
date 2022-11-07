import { configureStore } from '@reduxjs/toolkit'
import boardReducer from './boardSlice'
import dndReducer from './dndSlice'

export default configureStore({
  reducer: {
    board: boardReducer,
    dnd: dndReducer,
  },
})