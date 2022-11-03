import React from "react";

export default function Header({board}, onChange) {
    return (
        <div className='header'>
            <div className='header-logo'>
                <img src="https://2.downloader.disk.yandex.ru/preview/f45e3b23f97cf4c047bf5c28646a1d50bbd16a1893aaf412ee9cfbbbbc3ba5e7/inf/s3qLNl5FsEz_dos1HAcFbUrL_DHAMbn1EsbyLfGuPDsapdTTPitG-3aM-D3RT7vE-mqR3xPcHJSOQWQ5tPzo3A%3D%3D?uid=1581504016&filename=ggt-logo.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1581504016&tknv=v2&size=1920x969" alt="#" />
                <span>GigaTask</span>
            </div>
            <input type="text" name="board-name" value={board.name} onChange = {() => onChange()} />
        </div>
    )
}