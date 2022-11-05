import React from "react";

export default function Header({board, onChange}) {
    return (
        <div className='header'>
            <div className='header-logo'>
                <img src="https://downloader.disk.yandex.ru/preview/0621fab39abb84ba2c5d13c280be4125246da4758a8100bea80ba46f8d8b005d/63667dca/s3qLNl5FsEz_dos1HAcFbUrL_DHAMbn1EsbyLfGuPDsapdTTPitG-3aM-D3RT7vE-mqR3xPcHJSOQWQ5tPzo3A%3D%3D?uid=0&filename=ggt-logo.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048" alt="#" />
                <span>GigaTask</span>
            </div>
            <input type="text" name="board-name" value={board.name} onChange = {e => onChange(e.target.value)} />
        </div>
    )
}