import { combineReducers } from 'redux';
import AuthReducer from './auth';
import { reducer as FormReducer } from 'redux-form';
import NotesReducer from './notes';
import { SET_TOKEN } from '../actions';

const tokenInitialState = null;
const token = (state = tokenInitialState, action) => {
    switch(action.type) {
        case SET_TOKEN:
            return action.data;
        default:
            return state;
    }
}

const rootReducer = combineReducers({
   auth: AuthReducer,
   form: FormReducer,
   notes: NotesReducer,
   token: token,
});

export default rootReducer;