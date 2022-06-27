const viewTitleEle = document.getElementById('view-title');
const viewProfileImgEle = document.getElementById('view-profile-img');
const viewProfileNameEle = document.getElementById('view-profile-name');
const viewProfileTitleEle = document.getElementById('view-profile-title');
const viewProfileContentEle = document.getElementById('view-profile-content');
const viewCommentsContainerEle = document.getElementById('view-comments-container');

const setView = (viewTitle, imgSrc, name, title, content) => {
    viewTitleEle.innerText = viewTitle;
    viewProfileImgEle.setAttribute('src', imgSrc);
    viewProfileNameEle.innerText = name;
    viewProfileTitleEle.innerText = title;
    viewProfileContentEle.innerText = content;
};

setView('소프트웨어학과', 'assets/img/profile.png', 'gkgkgk', 'sdfskldfmlskmd', 'sdfnmlsmfdnls')

const testComments = [
    {
        name: '익익1',
        date: '어어제',
        content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
        subComments: [
            {
                name: '익익2',
                date: '어어제',
                content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
            },
            {
                name: '익익3',
                date: '어어제',
                content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
            },
            {
                name: '익익4',
                date: '어어제',
                content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
            },
        ]
    },
    {
        name: '익익5',
        date: '어어제',
        content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
        subComments: [
            {
                name: '익익6',
                date: '어어제',
                content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
            },
            {
                name: '익익8',
                date: '어어제',
                content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
            },
        ]
    },
    {
        name: '익익9',
        date: '어어제',
        content: 'ㅇㄴㅇ느ㅜ르나우라ㅣ',
        subComments: [
        ]
    },
]

const setComments = (comments) => {
    let commentsHTML = '';

    comments.forEach((comment) => {
        commentsHTML += `
        <div class="comments">
            <div class="comment d-flex mb-4 m-3">
                <div class="flex-shrink-0">
                    <div class="avatar avatar-sm rounded-circle">
                        <img class="avatar-img" src="assets/img/profile.png" alt="" class="img-fluid">
                    </div>
                </div>
                <div class="flex-grow-1 ms-2 ms-sm-3 ">
                <div class="comment-meta d-flex align-items-baseline">
                    <h6 class="me-2">${comment.name}</h6>
                    <span class="text-muted">${comment.date}</span>
                </div>
                <div class="comment-body">
                    ${comment.content}
                </div>
                ${comment.subComments.length > 0
                    ?
                    `
                    <div class="comment-replies bg-light p-3 mt-3 rounded">
                        ${comment.subComments.map((subComment) => `
                        <div class="reply d-flex mb-4">
                            <div class="flex-shrink-0">
                                <div class="avatar avatar-sm rounded-circle">
                                <img class="avatar-img" src="assets/img/profile.png" alt="" class="img-fluid">
                                </div>
                            </div>
                            <div class="flex-grow-1 ms-2 ms-sm-3">
                                <div class="reply-meta d-flex align-items-baseline">
                                <h6 class="mb-0 me-2">${subComment.name}</h6>
                                <span class="text-muted">${subComment.date}</span>
                                </div>
                                <div class="reply-body">
                                    ${subComment.content}
                                </div>
                            </div>
                        </div>
                        `)}
                    </div>
                    `
                    :
                    ''
                }
            </div>
        </div>
      
        
        
      </div>`
    });

    viewCommentsContainerEle.innerHTML = commentsHTML;
};

setComments(testComments)