const listBoardTitleEle=document.getElementById('list-board-title')

const setBoard=(boardTitle) => {
    listBoardTitleEle.innerText=boardTitle;
};

setBoard('소프트웨어 게시판')

const boardListEle=document.getElementById('board-list')

const testBoards = [
    {
        id: 40,
        title: '제목 1',
        content: '내용 1',
        writeDate: '언제씀 1',
        writerName: '작가 1',
        imgSrc: 'assets/img/comment.png',
        commentCount: 3,
    },
    {
        id: 41,
        title: '제목 2',
        content: '내용 2',
        writeDate: '언제씀 2',
        writerName: '작가 2',
        imgSrc: 'assets/img/comment.png',
        commentCount: 44,
    },
    {
        id: 42,
        title: '제목 5',
        content: '내용 5',
        writeDate: '언제씀 5',
        writerName: '작가 5',
        imgSrc: 'assets/img/comment.png',
        commentCount: 555,
    },
]

const setBoardList = (boards) => {
    let boardListHTML = '';

    boards.forEach((board) => {
        boardListHTML +=  `
        <a class="board" href="/view/${board.id}">
            <div class="title">${board.title}</div>
            <div class="content" >${board.content}</div>
            <div>
                <span class="write-date">${board.writeDate}</span>
                <span class="writer">${board.writerName}</span>
            </div>
            <div class="info">
                <img class="comment-img" src="${board.imgSrc}" />
                <span class="comment-count">${board.commentCount}</span>
            </div>
        </a>
        `
    });

    boardListEle.innerHTML = boardListHTML;
};

setBoardList(testBoards);