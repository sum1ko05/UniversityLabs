<?php
require_once __DIR__."/../vendor/autoload.php";

use PHPUnit\Framework\TestCase;

use function PHPUnit\Framework\assertEquals;

class PipelineErrorExampleTest extends TestCase
{
    public function testPipelineFailExample()
    {
        assertEquals(2, 1 + 2);
    }
}