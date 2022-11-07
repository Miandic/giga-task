import { createSlice } from '@reduxjs/toolkit'

export const dndSlice = createSlice({
  name: 'dnd',
  initialState: {
    dragTarget: null,
    dropTarget: null,
  },
  reducers: {
    setDragTarget: (state, action) => {
        state.dragTarget = action.payload.dragTarget;
    },
    setDropTarget: (state, action) => {
        state.dropTarget = action.payload.dropTarget;
    }
}
})

export const { setDragTarget, setDropTarget } = dndSlice.actions

export default dndSlice.reducer