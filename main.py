from canvas import Canvas
from logic import Logic


canvas = Canvas(height=15, width=20)
logic = Logic()


def start_loop(fps: int = 10):
    '''
    Starts the simulation\n
    Function is called n times a second (default 10), specified by the fps parameter.
    '''
    fps_in_ms = int(1000/fps)
    logic.next_frame(canvas.array)
    canvas.update_canvas()
    canvas.stop_id = canvas.root.after(fps_in_ms, lambda: start_loop(fps))

start_loop(fps=30)


canvas.root.mainloop()