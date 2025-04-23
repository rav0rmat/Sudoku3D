## `sudoku3d/core.py`

python
import numpy as np
import copy
import plotly.graph_objects as go

# Sudoku 3D helper functions

def is_valid(board: np.ndarray, z: int, x: int, y: int, num: int) -> bool:
    """Verifică dacă `num` poate fi plasat la poziția (z,x,y)."""
    # rând, coloană, strat
    for yy in range(4):
        if yy != y and board[z, x, yy] == num:
            return False
    for xx in range(4):
        if xx != x and board[z, xx, y] == num:
            return False
    for zz in range(4):
        if zz != z and board[zz, x, y] == num:
            return False
    # bloc 2x2x2
    xb, yb, zb = (x//2)*2, (y//2)*2, (z//2)*2
    for zz in range(zb, zb+2):
        for xx in range(xb, xb+2):
            for yy in range(yb, yb+2):
                if (zz,xx,yy) != (z,x,y) and board[zz,xx,yy] == num:
                    return False
    return True


def solve(board: np.ndarray) -> bool:
    """Rezolvă recursiv Sudoku 3D prin backtracking."""
    for z in range(4):
        for x in range(4):
            for y in range(4):
                if board[z,x,y] == 0:
                    for num in range(1,5):
                        if is_valid(board, z, x, y, num):
                            board[z,x,y] = num
                            if solve(board):
                                return True
                            board[z,x,y] = 0
                    return False
    return True


def count_solutions(board: np.ndarray, limit: int=2) -> int:
    """Numără soluțiile unice până la `limit`."""
    solutions = [0]
    def backtrack(b):
        if solutions[0] >= limit:
            return
        for z in range(4):
            for x in range(4):
                for y in range(4):
                    if b[z,x,y] == 0:
                        for num in range(1,5):
                            if is_valid(b, z, x, y, num):
                                b[z,x,y] = num
                                backtrack(b)
                                b[z,x,y] = 0
                        return
        solutions[0] += 1
    backtrack(board.copy())
    return solutions[0]


def generate_complete_sudoku() -> np.ndarray:
    """Generează un board complet rezolvabil."""
    board = np.zeros((4,4,4), dtype=int)
    solve(board)
    return board


def generate_playable_puzzle(solved_board: np.ndarray, difficulty: str='medium') -> np.ndarray:
    """Generează puzzle cu un singur path de soluție."""
    puzzle = solved_board.copy()
    num_remove = {'beginner':32,'easy':36,'medium':40,'hard':48}[difficulty]
    coords = [(z,x,y) for z in range(4) for x in range(4) for y in range(4)]
    np.random.shuffle(coords)
    removed = 0
    for z,x,y in coords:
        if removed >= num_remove:
            break
        temp = puzzle[z,x,y]
        puzzle[z,x,y] = 0
        if count_solutions(puzzle) != 1:
            puzzle[z,x,y] = temp
        else:
            removed += 1
    return puzzle


def draw_board(board: np.ndarray, initial_board: np.ndarray, highlight: tuple=None) -> go.Figure:
    """Desenează board-ul 3D folosind Plotly."""
    x,y,z,val,color = [],[],[],[],[]
    for zi in range(4):
        for xi in range(4):
            for yi in range(4):
                x.append(xi); y.append(yi); z.append(zi)
                v = board[zi,xi,yi]
                val.append(v)
                if highlight==(zi,xi,yi): color.append('orange')
                elif initial_board is not None and initial_board[zi,xi,yi]!=0: color.append('darkblue')
                elif v!=0: color.append('lightgreen')
                else: color.append('lightgray')
    fig = go.Figure(data=go.Scatter3d(x=x,y=y,z=z,mode='markers+text',
        marker=dict(size=10,color=color,opacity=0.9),
        text=[str(v) if v>0 else '' for v in val],
        textfont=dict(color='white',size=14),textposition='middle center'))
    fig.update_layout(scene=dict(xaxis=dict(range=[-.5,3.5]),
                                 yaxis=dict(range=[-.5,3.5]),
                                 zaxis=dict(range=[-.5,3.5)]),
                      margin=dict(l=0,r=0,b=0,t=0),height=800)
    return fig

