//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var LineModel = require('./Line.autogen.js').LineModel;


class LineLoopModel extends LineModel {

    defaults() {
        return _.extend(LineModel.prototype.defaults.call(this), {

            type: "LineLoop",

        });
    }

    constructThreeObject() {

        var result = new THREE.LineLoop(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry'),
            this.convertThreeTypeModelToThree(this.get('material'), 'material')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LineModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['type'] = null;


    }
}

LineLoopModel.model_name = 'LineLoopModel';
LineLoopModel.serializers = {
    ...LineModel.serializers,
};

module.exports = {
    LineLoopModel: LineLoopModel,
};
