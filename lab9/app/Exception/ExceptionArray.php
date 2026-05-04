<?php

namespace App\Exception;

use Exception;

class ExceptionArray extends Exception
{
    private Array $exceptions;

    public function __construct(string $message, 
                                int $code = 0, 
                                ?Exception $previous_exception = null, 
                                Array $exceptions = array('params')) 
    {
        parent::__construct($message, $code, $previous_exception);

        $this->exceptions = $exceptions; 
    }

    public function GetExceptions(): Array { return $this->exceptions; }
}