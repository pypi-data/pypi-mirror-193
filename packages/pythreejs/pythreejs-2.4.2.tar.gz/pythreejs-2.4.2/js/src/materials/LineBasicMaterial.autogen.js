//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var MaterialModel = require('./Material.js').MaterialModel;


class LineBasicMaterialModel extends MaterialModel {

    defaults() {
        return _.extend(MaterialModel.prototype.defaults.call(this), {

            color: "#ffffff",
            lights: false,
            linewidth: 1,
            linecap: "round",
            linejoin: "round",
            type: "LineBasicMaterial",

        });
    }

    constructThreeObject() {

        var result = new THREE.LineBasicMaterial(
            {
                color: this.convertColorModelToThree(this.get('color'), 'color'),
                lights: this.convertBoolModelToThree(this.get('lights'), 'lights'),
                linewidth: this.convertFloatModelToThree(this.get('linewidth'), 'linewidth'),
                linecap: this.get('linecap'),
                linejoin: this.get('linejoin'),
                type: this.get('type'),
            }
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        MaterialModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['color'] = 'convertColor';
        this.property_converters['lights'] = 'convertBool';
        this.property_converters['linewidth'] = 'convertFloat';
        this.property_converters['linecap'] = null;
        this.property_converters['linejoin'] = null;
        this.property_converters['type'] = null;


    }
}

LineBasicMaterialModel.model_name = 'LineBasicMaterialModel';
LineBasicMaterialModel.serializers = {
    ...MaterialModel.serializers,
};

module.exports = {
    LineBasicMaterialModel: LineBasicMaterialModel,
};
