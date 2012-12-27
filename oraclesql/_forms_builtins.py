import re
import urllib

__all__ = ['FORMS_BUILTINS']

# Oracle Forms specific section, based on Oracle Forms Builder 6i documentation
FORMS_BUILTINS = ['ABORT_QUERY',
                  'ADD_GROUP_COLUMN',
                  'ADD_GROUP_ROW',
                  'ADD_LIST_ELEMENT',
                  'ADD_OLEARGS',
                  'ADD_PARAMETER',
                  'APPLICATION_PARAMETER',
                  'BELL',
                  'BLOCK_MENU',
                  'BREAK',
                  'CALL_FORM',
                  'CALL_INPUT',
                  'CALL_OLE',
                  'CALL_OLE_CHAR',
                  'CALL_OLE_NUM',
                  'CALL_OLE_OBJ',
                  'CALL_OLE_VAR',
                  'CANCEL_REPORT_OBJECT',
                  'CHECK_RECORD_UNIQUENESS',
                  'CHECKBOX_CHECKED',
                  'CHECKED',
                  'CLEAR_BLOCK',
                  'CLEAR_EOL',
                  'CLEAR_FORM',
                  'CLEAR_ITEM',
                  'CLEAR_LIST',
                  'CLEAR_MESSAGE',
                  'CLEAR_RECORD',
                  'CLOSE_FORM',
                  'COMMIT_FORM',
                  'CONVERT_OTHER_VALUE',
                  'COPY',
                  'COPY_REGION',
                  'COPY_REPORT_OUTPUT',
                  'COUNT_QUERY',
                  'CREATE_GROUP',
                  'CREATE_GROUP_FROM_QUERY',
                  'CREATE_OLEOBJ',
                  'CREATE_PARAMETER_LIST',
                  'CREATE_QUERIED_RECORD',
                  'CREATE_RECORD',
                  'CREATE_TIMER',
                  'CREATE_VAR',
                  'CUT_REGION',
                  'DBMS_ERROR_CODE',
                  'DBMS_ERROR_TEXT',
                  'DEBUG_MODE',
                  'DEFAULT_VALUE',
                  'DELETE_GROUP',
                  'DELETE_GROUP_ROW',
                  'DELETE_LIST_ELEMENT',
                  'DELETE_PARAMETER',
                  'DELETE_RECORD',
                  'DELETE_TIMER',
                  'DESTROY_PARAMETER_LIST',
                  'DESTROY_VARIANT',
                  'DISPATCH_EVENT',
                  'DISPLAY_ERROR',
                  'DISPLAY_ITEM',
                  'DOWN',
                  'DO_KEY',
                  'DUMMY_REFERENCE',
                  'DUPLICATE_ITEM',
                  'DUPLICATE_RECORD',
                  'EDIT_TEXTITEM',
                  'ENFORCE_COLUMN_SECURITY',
                  'ENTER',
                  'ENTER_QUERY',
                  'ERASE',
                  'ERROR_CODE',
                  'ERROR_TEXT',
                  'ERROR_TYPE',
                  'EXECUTE_QUERY',
                  'EXECUTE_TRIGGER',
                  'EXIT_FORM',
                  'FETCH_RECORDS',
                  'FIND_ALERT',
                  'FIND_BLOCK',
                  'FIND_CANVAS',
                  'FIND_COLUMN',
                  'FIND_EDITOR',
                  'FIND_FORM',
                  'FIND_GROUP',
                  'FIND_ITEM',
                  'FIND_LOV',
                  'FIND_MENU_ITEM',
                  'FIND_RELATION',
                  'FIND_REPORT_OBJECT',
                  'FIND_TAB_PAGE',
                  'FIND_TIMER',
                  'FIND_VIEW',
                  'FIND_WINDOW',
                  'FIRST_RECORD',
                  'FORM_FAILURE',
                  'FORM_FATAL',
                  'FORM_SUCCESS',
                  'FORMS_DDL',
                  'FORMS_OLE.ACTIVATE_SERVER',
                  'FORMS_OLE.CLOSE_SERVER',
                  'FORMS_OLE.EXEC_VERB',
                  'FORMS_OLE.FIND_OLE_VERB',
                  'FORMS_OLE.GET_INTERFACE_POINTER',
                  'FORMS_OLE.GET_VERB_COUNT',
                  'FORMS_OLE.GET_VERB_NAME',
                  'FORMS_OLE.INITIALIZE_CONTAINER',
                  'FORMS_OLE.SERVER_ACTIVE',
                  'GENERATE_SEQUENCE_NUMBER',
                  'GET_APPLICATION_PROPERTY',
                  'GET_BLOCK_PROPERTY',
                  'GET_CANVAS_PROPERTY',
                  'GET_FILE_NAME',
                  'GET_FORM_PROPERTY',
                  'GET_GROUP_CHAR_CELL',
                  'GET_GROUP_DATE_CELL',
                  'GET_GROUP_NUMBER_CELL',
                  'GET_GROUP_RECORD_NUMBER',
                  'GET_GROUP_ROW_COUNT',
                  'GET_GROUP_SELECTION',
                  'GET_GROUP_SELECTION_COUNT',
                  'GET_INTERFACE_POINTER ',
                  'GET_ITEM_INSTANCE_PROPERTY',
                  'GET_ITEM_PROPERTY',
                  'GET_LIST_ELEMENT_COUNT',
                  'GET_LIST_ELEMENT_LABEL',
                  'GET_LIST_ELEMENT_VALUE',
                  'GET_LOV_PROPERTY',
                  'GET_MENU_ITEM_PROPERTY',
                  'GET_MESSAGE',
                  'GET_OLEARG_CHAR',
                  'GET_OLEARG_NUM',
                  'GET_OLEARG_OBJ',
                  'GET_OLEARG_VAR',
                  'GET_OLE_MEMBERID',
                  'GET_OLE_CHAR',
                  'GET_OLE_NUM',
                  'GET_OLE_OBJ',
                  'GET_OLE_VAR',
                  'GET_PARAMETER_ATTR',
                  'GET_PARAMETER_LIST',
                  'GET_RADIO_BUTTON_PROPERTY',
                  'GET_RECORD_PROPERTY',
                  'GET_RELATION_PROPERTY',
                  'GET_REPORT_OBJECT_PROPERTY',
                  'GET_TAB_PAGE_PROPERTY',
                  'GET_VAR_BOUNDS',
                  'GET_VAR_DIMS',
                  'GET_VAR_TYPE',
                  'GET_VIEW_PROPERTY',
                  'GET_WINDOW_PROPERTY',
                  'GO_BLOCK',
                  'GO_FORM',
                  'GO_ITEM',
                  'GO_RECORD',
                  'HELP',
                  'HIDE_MENU',
                  'HIDE_VIEW',
                  'HIDE_WINDOW',
                  'HOST',
                  'ID_NULL',
                  'IMAGE_SCROLL',
                  'IMAGE_ZOOM',
                  'INIT_OLEARGS',
                  'INITIALIZE_CONTAINER ',
                  'INSERT_RECORD',
                  'ISSUE_ROLLBACK',
                  'ISSUE_SAVEPOINT',
                  'ITEM_ENABLED',
                  'LAST_OLE_ERROR',
                  'LAST_OLE_EXCEPTION',
                  'LAST_RECORD',
                  'LIST_VALUES',
                  'LOCK_RECORD',
                  'LOGON',
                  'LOGON_SCREEN',
                  'LOGOUT',
                  'MENU_CLEAR_FIELD',
                  'MENU_NEXT_FIELD',
                  'MENU_PARAMETER',
                  'MENU_PREVIOUS_FIELD',
                  'MENU_REDISPLAY',
                  'MENU_SHOW_KEYS',
                  'MESSAGE',
                  'MESSAGE_CODE',
                  'MESSAGE_TEXT',
                  'MESSAGE_TYPE',
                  'MOVE_WINDOW',
                  'NAME_IN',
                  'NEW_FORM',
                  'NEXT_BLOCK',
                  'NEXT_ITEM',
                  'NEXT_FORM',
                  'NEXT_KEY',
                  'NEXT_MENU_ITEM',
                  'NEXT_RECORD',
                  'NEXT_SET',
                  'OLEVAR_EMPTY',
                  'OPEN_FORM',
                  'PASTE_REGION',
                  'PAUSE',
                  'PECS.ADD_CLASS',
                  'PECS.ADD_EVENT',
                  'PECS.COLLECTOR',
                  'PECS.DISABLE_CLASS',
                  'PECS.ENABLE_CLASS',
                  'PECS.END_EVENT',
                  'PECS.POINT_EVENT',
                  'PECS.START_EVENT',
                  'PLAY_SOUND',
                  'POPULATE_GROUP',
                  'POPULATE_GROUP_WITH_QUERY',
                  'POPULATE_LIST',
                  'POST',
                  'PREVIOUS_BLOCK',
                  'PREVIOUS_FORM',
                  'PREVIOUS_ITEM',
                  'PREVIOUS_MENU',
                  'PREVIOUS_MENU_ITEM',
                  'PREVIOUS_RECORD',
                  'PRINT',
                  'PTR_TO_VAR',
                  'QUERY_PARAMETER',
                  'READ_IMAGE_FILE',
                  'READ_SOUND_FILE',
                  'RECALCULATE',
                  'REDISPLAY',
                  'RELEASE_OBJ',
                  'REPLACE_CONTENT_VIEW',
                  'REPLACE_MENU',
                  'REPORT_OBJECT_STATUS',
                  'RESET_GROUP_SELECTION',
                  'RESIZE_WINDOW',
                  'RETRIEVE_LIST',
                  'RUN_PRODUCT',
                  'RUN_REPORT_OBJECT',
                  'SCROLL_DOWN',
                  'SCROLL_UP',
                  'SCROLL_VIEW',
                  'SELECT_ALL',
                  'SELECT_RECORDS',
                  'SET_ALERT_BUTTON_PROPERTY',
                  'SET_ALERT_PROPERTY',
                  'SET_APPLICATION_PROPERTY',
                  'SET_BLOCK_PROPERTY',
                  'SET_CANVAS_PROPERTY',
                  'SET_FORM_PROPERTY',
                  'SET_GROUP_CHAR_CELL',
                  'SET_GROUP_DATE_CELL',
                  'SET_GROUP_NUMBER_CELL',
                  'SET_GROUP_SELECTION',
                  'SET_INPUT_FOCUS',
                  'SET_ITEM_INSTANCE_PROPERTY',
                  'SET_ITEM_PROPERTY',
                  'SET_LOV_COLUMN_PROPERTY',
                  'SET_LOV_PROPERTY',
                  'SET_MENU_ITEM_PROPERTY',
                  'SET_OLE',
                  'SET_PARAMETER_ATTR',
                  'SET_RADIO_BUTTON_PROPERTY',
                  'SET_RECORD_PROPERTY',
                  'SET_RELATION_PROPERTY',
                  'SET_REPORT_OBJECT_PROPERTY',
                  'SET_TAB_PAGE_PROPERTY',
                  'SET_TIMER',
                  'SET_VAR',
                  'SET_VIEW_PROPERTY',
                  'SET_WINDOW_PROPERTY',
                  'SHOW_ALERT',
                  'SHOW_EDITOR',
                  'SHOW_KEYS',
                  'SHOW_LOV',
                  'SHOW_MENU',
                  'SHOW_VIEW',
                  'SHOW_WINDOW',
                  'SYNCHRONIZE',
                  'TERMINATE',
                  'TO_VARIANT',
                  'UNSET_GROUP_SELECTION',
                  'UP',
                  'UPDATE_CHART',
                  'UPDATE_RECORD',
                  'USER_EXIT',
                  'VALIDATE',
                  'VARPTR_TO_VAR',
                  'VAR_TO_TABLE',
                  'VAR_TO_CHAR',
                  'VAR_TO_NUMBER',
                  'VAR_TO_OBJ',
                  'VAR_TO_VARPTR',
                  'VBX.FIRE_EVENT',
                  'VBX.GET_PROPERTY',
                  'VBX.GET_VALUE_PROPERTY',
                  'VBX.INVOKE_METHOD',
                  'VBX.SET_PROPERTY',
                  'VBX.SET_VALUE_PROPERTY',
                  'WEB.SHOW_DOCUMENT',
                  'WHERE_DISPLAY',
                  'WRITE_IMAGE_FILE',
                  'WRITE_SOUND_FILE']